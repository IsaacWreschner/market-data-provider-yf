# iw_market_data_provider_yf

A lightweight Python library to fetch historical market data using Yahoo Finance (`yfinance`) with flexible timeframes and symbol support.

---

## 📦 Overview

This library allows you to retrieve market data from Yahoo Finance and return it in multiple formats:

- **Pandas DataFrame**
- **Array of close (or open) prices**
- **Array of candlestick bars**

It supports a wide range of timeframes and financial instruments. It also caches previously fetched data locally to avoid redundant API calls.

---

## ⏱️ Supported Timeframes

| ID   | Description   | Interval (ms) |
|------|---------------|---------------|
| 1m   | 1 Minute      | 60,000        |
| 2m   | 2 Minutes     | 120,000       |
| 5m   | 5 Minutes     | 300,000       |
| 15m  | 15 Minutes    | 900,000       |
| 30m  | 30 Minutes    | 1,800,000     |
| 60m  | 1 Hour        | 3,600,000     |
| 90m  | 1.5 Hours     | 5,400,000     |
| 1d   | 1 Day         | 86,400,000    |
| 5d   | 5 Days        | 432,000,000   |
| 1wk  | 1 Week        | 604,800,000   |
| 1mo  | 1 Month       | 2,592,000,000 |
| 3mo  | 3 Months      | 7,776,000,000 |

---

## 💹 Supported Symbols

Includes indices, forex pairs, commodities, cryptocurrencies, ETFs, and stocks such as:

- `^IXIC`, `^GSPC`, `^DJI`, `^RUT`
- `EURUSD=X`, `JPY=X`, `GBPUSD=X`, `AUDUSD=X`, `USDCAD=X`
- `GC=F`, `SI=F`, `CL=F`
- `BTC-USD`, `ETH-USD`
- `SPY`, `QQQ`, `VTI`
- `AAPL`, `AMZN`, `GOOGL`, `TSLA`

Each symbol also includes metadata such as `pip_point`.

---

## 🧠 Features

- ✅ Simple interface to fetch historical OHLC data
- ✅ Supports multiple return types: DataFrame, arrays of ticks or candlesticks
- ✅ Built-in caching to prevent redundant network calls
- ✅ Timeframe and symbol validation included

---

## 🛠 Local Installation

This package is not yet published to PyPI. To use it locally:

1. Clone the repository or copy the library folder to your project.



2. Choose one of the following build options:

   - **Option 1: Recommended — Use the reload script**

     - On **Linux/macOS**:
       ```bash
       ./reload-package.sh
       ```
     - On **Windows (Command Prompt)**:
       ```cmd
       reload-package.bat
       ```


     These scripts will build and reinstall the package automatically.

   - **Option 2: Manual Build and Install**

     First, install the build module (if not already installed):
     ```bash
     pip install build
     ```

     Build the package:
     ```bash
     python -m build
     ```

     Then install it in editable mode:
     ```bash
     pip install -e .
     ```

## 🚀 Usage

Import the main interface and fetch data:

```python
from iw_market_data_provider_yf import MarketData

# Fetch 1-minute data for AAPL from July 1 to July 10, 2024
md = MarketData(
        symbol="AAPL",
        start_date="2024-07-01",
        end_date="2024-07-10",
        timeframe="1m"
        margin=1
    )

ticks = md.as_ticks() # [{datetime, price, buy_price, sell_price, index }, ...]
candlesticks = md.as_candlesticks()  # [{datetime, open, close, low, index }, ...]
df = md.as_df() # For manipulation
```

Built-in caching ensures that repeated requests for the same data are served instantly from disk.
