import duckdb
import polars as pl
from log import logger

def load(df):
    conn = duckdb.connect("crypto.db")
    conn.register("df", df)
    conn.execute("CREATE OR REPLACE TABLE coins AS SELECT * FROM df")
    conn.close()
    logger.info("Load completed")