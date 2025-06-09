import yfinance as yf
from SYMBOLS import SYMBOLS
from TIMEFRAMES import TIMEFRAMES
from datetime import datetime, timedelta
import subprocess
import json
import pandas as pd
from cache import store_market_data, retrieve_market_data
from calendar import monthrange

def snap_date_to_month_start(dt: datetime) -> datetime:
    return dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

def snap_date_to_month_end(dt: datetime) -> datetime:
    last_day = monthrange(dt.year, dt.month)[1]
    return dt.replace(day=last_day, hour=23, minute=59, second=59, microsecond=999999)


def create_period_str(start_datetime: datetime, end_datetime: datetime) -> (int, int):
    period1 = int(start_datetime.timestamp())
    period2 = int(end_datetime.timestamp())
    return period1, period2


def fetch_market_data(symbol: str, timeframe: str, start_datetime: datetime, end_datetime: datetime) -> (pd.DataFrame | None):
    valid_symbols = SYMBOLS
    valid_timeframes = TIMEFRAMES

    if symbol not in valid_symbols:
        raise ValueError(f"Symbol '{symbol}' not found in supported instruments.")
    if timeframe not in valid_timeframes:
        raise ValueError(f"Timeframe '{timeframe}' is not valid.")

    # Try to retrieve locally
    local_data = retrieve_market_data(symbol, start_datetime, end_datetime, timeframe)
    if local_data is not None:
        return local_data

    # Snap to full month
    month_start, month_end = snap_date_to_month_start(start_datetime), snap_date_to_month_end(end_datetime)
    print(f"[DEBUG] Fetching data from {month_start} to {month_end}")
    period1_tostr, period2_tostr = create_period_str(month_start, month_end)

    # Fetch from Yahoo Finance
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval={timeframe}&period1={period1_tostr}&period2={period2_tostr}"
    print(f"[DEBUG] Fetching data from {url}")
    cmd = ["curl", "-s", "-H", "User-Agent: Mozilla/5.0", url]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"curl failed: {result.stderr}")

    try:
        data = json.loads(result.stdout)
        chart = data['chart']['result'][0]
        timestamps = chart['timestamp']
        indicators = chart['indicators']['quote'][0]

        df = pd.DataFrame({
            'Date': [datetime.fromtimestamp(ts) for ts in timestamps],
            'Open': indicators['open'],
            'High': indicators['high'],
            'Low': indicators['low'],
            'Close': indicators['close'],
            'Volume': indicators['volume']
        })

        df.set_index('Date', inplace=True)
        df[['Open', 'High', 'Low', 'Close', 'Volume']] = df[['Open', 'High', 'Low', 'Close', 'Volume']].ffill()
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error parsing curl response: {e}")
        return None

    # Filter the DataFrame to the requested time range (to avoid having previous day of month data )
    df = df.loc[(df.index >= month_start) & (df.index <= month_end)]
    if df.empty:
        raise ValueError(f"No data found for {symbol} between {start_datetime} and {end_datetime}")
    store_market_data(df, symbol, timeframe)
    return retrieve_market_data(symbol, start_datetime, end_datetime, timeframe)
