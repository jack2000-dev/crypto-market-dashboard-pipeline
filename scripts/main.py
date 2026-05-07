import extract
import transform
import load
import log
import time


def main():
    try:
        market = extract.fetch_market()
        ohlc_list = []
        
        # Loop for fetch data (Extract.py)
        for coin in market:
            ohlc = extract.fetch_ohlc(coin["id"], "usd", 7)
            ohlc_list.append({
                "id": coin["id"], 
                "name": coin["name"], 
                "symbol": coin["symbol"], 
                "ohlc": ohlc
                })

        market_df = transform.transform_market(market)
        ohlc_df = transform.transform_ohlc(ohlc_list)
        load.load(market_df, ohlc_df)
        log.logger.info("Main: Pipeline completed")
        return market_df, ohlc_df
    except Exception as e:
        log.logger.error(f"Main: {e}")


if __name__ == "__main__":
    df = main()
    