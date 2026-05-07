# Scripts

Reusable Python helpers.

| Script | Command | Purpose |
|--------|---------|---------|
| `paths.py` | `uv run python scripts/paths.py` | Print all resolved project paths (sanity check) |
| `snapshot.py` | `make snapshot` | Generate `docs/data_dictionary.md` from CSV/Parquet in `data/raw/` and `data/processed/` |

`paths.py` is the core helper — every notebook and script imports from it. See its module docstring for usage examples and notebook setup.

## Adding your own scripts

- Place reusable Python helpers here (anything imported by notebooks or other scripts).
- One-off analysis logic stays in notebooks.
- If a script grows beyond ~150 lines, consider splitting into a module.

## File structure

```
crypto-market-dashboard-pipeline/
├── main.py          # orchestrator
├── extract.py       # fetch market + OHLC data
├── transform.py     # clean, calculate MA & % change
├── load.py          # save to DuckDB (2 tables)
├── scheduler.py     # run every hour
├── log.py           # shared logger
└── .env             # API key (.gitignore - DO NOT COMMIT)
```