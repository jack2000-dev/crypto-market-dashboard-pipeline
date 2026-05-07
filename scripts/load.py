import duckdb
import polars as pl
from pathlib import Path
from log import logger

DB_PATH = str(Path(__file__).resolve().parent.parent / "data" / "processed" / "crypto.db")

def load(market_df, ohlc_df):
    conn = duckdb.connect(DB_PATH)
    conn.register("market_df", market_df)
    conn.register("ohlc_df", ohlc_df)
    conn.execute("CREATE OR REPLACE TABLE market AS SELECT * FROM market_df")
    conn.execute("CREATE OR REPLACE TABLE ohlc AS SELECT * FROM ohlc_df")
    conn.close()
    logger.info("Load completed")