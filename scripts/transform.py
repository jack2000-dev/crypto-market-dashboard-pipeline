# id, symbol, name, current_price, market_cap, total_volume, high_24h, low_24h
import polars as pl
from log import logger

def transform(data: list) -> pl.DataFrame:
    df = pl.DataFrame(data)

    df = df.select(["id", "symbol", "name", "current_price", "market_cap", "total_volume", "high_24h", "low_24h"])

    # Filter out market cap == 0
    df = df.filter(pl.col("market_cap") > 0)

    # price_range_24h = high_24h - low_24h
    df = df.with_columns([(pl.col("high_24h") - pl.col("low_24h")).alias("price_range_24h")])

    return df
    logger.info("Transform completed")