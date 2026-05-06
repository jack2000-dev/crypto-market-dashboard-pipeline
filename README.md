# Crypto Market Dashboard Pipeline

> *An automated ETL pipeline that fetches top cryptocurrency metrics hourly, processes them with Polars, and stores them in DuckDB for dashboarding.*

**Type:** `#Data Pipeline` `#ETL` | **Tools:** `#Python` `#Polars` `#DuckDB` | **Period:** `2026-05`

---

## Key Insights

**1. Reliable Data Ingestion** — The pipeline successfully automates the extraction of live market data from the CoinGecko API on an hourly schedule, eliminating manual data pulls.

**2. Efficient Transformation** — By leveraging Polars, the pipeline efficiently cleans the data, filtering out zero-market-cap coins and calculating dynamic fields like the 24-hour price range.

**3. Lightweight Storage** — Processed data is loaded into a local DuckDB database (`crypto.db`), providing a highly performant and easy-to-query analytical backend without the overhead of a traditional RDBMS.

---

## Overview

<!-- Context → Problem → Approach → Outcome. 3–4 sentences. -->

To support a real-time crypto market dashboard, there was a need for a reliable and scheduled stream of cryptocurrency market data. Manually fetching and cleaning this data was tedious and error-prone. This project implemented an end-to-end Python ETL pipeline that extracts data from the CoinGecko API, transforms it using Polars for high performance, and loads it into a DuckDB database. The outcome is a continuously updated, query-ready local database that serves as the backbone for downstream analytics and dashboarding.

---

## Data Source

| Field | Details |
|-------|---------|
| **Source** | CoinGecko API (`/coins/markets`) |
| **Format** | JSON to Polars DataFrame |
| **Size** | 10 rows (Top 10 coins by market cap) per fetch |
| **Period** | Current (Live Data) |
| **Key fields** | `id`, `symbol`, `current_price`, `market_cap` |

---

## Limitations

- Data is currently limited to the top 10 cryptocurrencies by market cap per page request due to API configuration.
- The pipeline relies on the public CoinGecko API, which may be subject to rate limits or intermittent downtime.
- Historical data is overwritten each hour (`CREATE OR REPLACE TABLE`), so the pipeline tracks the *current* state rather than a time-series history.

---

## Files

| File | Description |
|------|-------------|
| [`scripts/extract.py`](scripts/extract.py) | Fetches data from CoinGecko API |
| [`scripts/transform.py`](scripts/transform.py) | Cleans and formats data using Polars |
| [`scripts/load.py`](scripts/load.py) | Loads data into DuckDB (`crypto.db`) |
| [`scripts/scheduler.py`](scripts/scheduler.py) | Runs the pipeline hourly |
| [`reports/REPORT.md`](reports/REPORT.md) | Full structured report |

---

*Author: **jack2000-dev** | Last updated: 2026-05-06*
