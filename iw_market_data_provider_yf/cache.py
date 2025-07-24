import os
import pandas as pd
from datetime import datetime
from typing import Union


def store_market_data(df: pd.DataFrame, symbol: str, timeframe: str, base_dir: str = None) -> None:
    if base_dir is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.join(current_dir, ".cache")

    df = df.copy()
    df.reset_index(inplace=True)
    df.rename(columns={"Date": "Date", "Open": "Open", "High": "High", "Low": "Low", "Close": "Close"}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])

    symbol_dir = os.path.join(base_dir, symbol)
    os.makedirs(symbol_dir, exist_ok=True)

    for (year, month), group in df.groupby([df['Date'].dt.year, df['Date'].dt.month]):
        year_dir = os.path.join(symbol_dir, str(year))
        month_dir = os.path.join(year_dir, f"{month:02}")
        os.makedirs(month_dir, exist_ok=True)

        file_path = os.path.join(month_dir, f"{timeframe}.data.csv")
        group = group[['Date', 'High', 'Low', 'Open', 'Close']]
        group.to_csv(file_path, index=False)
        print(f"Saved data to {file_path}")


def retrieve_market_data(symbol: str, start_date: Union[str, datetime], end_date: Union[str, datetime], timeframe: str, base_dir: str = ".cache") -> Union[pd.DataFrame, None]:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(current_dir, base_dir)

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    all_data = []
    symbol_dir = os.path.join(base_dir, symbol)
    if not os.path.exists(symbol_dir):
        print(f"Symbol directory not found: {symbol_dir}")
        return None

    for year in range(start_date.year, end_date.year + 1):
        for month in range(1, 13):
            month_start = datetime(year, month, 1)
            if month_start > end_date:
                break
            if month_start < start_date.replace(day=1):
                continue

            file_path = os.path.join(symbol_dir, str(year), f"{month:02}", f"{timeframe}.data.csv")

            if not os.path.isfile(file_path):
                print(f"[DEBUG] Missing file for {year}-{month:02}: {file_path}")
                return None  # Critical: missing one month's file means incomplete data

            df = pd.read_csv(file_path, parse_dates=['Date'])
            print(f"[DEBUG] Loaded {len(df)} rows from {file_path}")

            filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
            print(f"[DEBUG] Filtered data from {filtered_df['Date'].min()} to {filtered_df['Date'].max()}")
            all_data.append(filtered_df)

    if not all_data:
        print("[INFO] No data loaded.")
        return None

    print(f"[INFO] Retrieved data from {len(all_data)} files.")
    return pd.concat(all_data, ignore_index=True).sort_values(by="Date")

