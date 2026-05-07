# id, symbol, name, current_price, market_cap, total_volume, high_24h, low_24h
import polars as pl
from log import logger


def transform_market(market: list) -> pl.DataFrame:
    df = pl.DataFrame(market)

    df = df.select(
        [
            "id",
            "symbol",
            "name",
            "current_price",
            "market_cap",
            "total_volume",
            "high_24h",
            "low_24h",
        ]
    )

    # Filter out market cap == 0
    df = df.filter(pl.col("market_cap") > 0)

    # price_range_24h = high_24h - low_24h
    df = df.with_columns(
        [(pl.col("high_24h") - pl.col("low_24h")).alias("price_range_24h")]
    )

    logger.info("Transform: market completed")
    return df


def transform_ohlc(ohlc: list) -> pl.DataFrame:
    rows = []
    for coin in ohlc:
        for row in coin["ohlc"]:
            timestamp, open, high, low, close = row
            rows.append(
                {
                    "id": coin["id"],
                    "symbol": coin["symbol"],
                    "name": coin["name"],
                    "timestamp": timestamp,
                    "open": open,
                    "high": high,
                    "low": low,
                    "close": close,
                }
            )
    df = pl.DataFrame(rows).with_columns(
        pl.col("timestamp").cast(pl.Datetime("ms")).alias("timestamp")
    )
    # Moving average
    df = df.with_columns(
        [(pl.col("close").rolling_mean(window_size=7).over("id")).alias("ma_7d")]
    )
    # Percent Change ((current_close - previous_close) / previous_close) * 100
    df = df.with_columns(
        [
            (pl.col("close").diff() / pl.col("close").shift(1))
            .over("id")
            .alias("pct_change_24h")
        ]
    )
    logger.info("Transform: OHLC completed")
    return df
