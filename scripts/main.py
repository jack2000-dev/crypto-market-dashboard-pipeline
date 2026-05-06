from extract import fetch_data
from transform import transform
from load import load
from log import logger  

def main():
    try:
        data = fetch_data()
        df = transform(data)
        load(df)
        logger.info("Main: Pipeline completed")
        return df
    except Exception as e:
        logger.error(f"Main: {e}")

if __name__ == "__main__":
    df = main()
    