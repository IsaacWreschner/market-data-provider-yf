from datetime import datetime
import pandas as pd
from json import loads
from typing import List
from .fetch import fetch_market_data
from .models.tick import tick
from .models.candlestick import candlestick  
from .SYMBOLS import SYMBOLS
import math

class MarketData:
    _raw_data: pd.DataFrame = None
    _raw_data_copy: pd.DataFrame = None

    def __init__(self, symbol: str, timeframe: str, start_datetime: datetime, end_datetime: datetime, margin: float = 0.5):
        self._timeframe = timeframe
        self._pip_point = self._get_pip_point(symbol) 

        self._raw_data = fetch_market_data(
            symbol=symbol,
            timeframe=timeframe,
            start_datetime=start_datetime,
            end_datetime=end_datetime
        )
        self.__enhance_data(margin=margin)

    def __enhance_data(self, margin: float = 0.5) -> None:
        pip_adjustment = margin * self._pip_point
        decimals = abs(int(round(-math.log10(self._pip_point)))) + 1 # Determine number of decimals from pip point

        self._raw_data_copy = self._raw_data.copy()
        self._raw_data_copy['price_as_tick'] = self._raw_data['Open'].round(decimals)
        self._raw_data_copy['buy_price_as_tick'] = (self._raw_data_copy['price_as_tick'] + pip_adjustment).round(decimals)
        self._raw_data_copy['sell_price_as_tick'] = (self._raw_data_copy['price_as_tick'] - pip_adjustment).round(decimals)
        try:
           self._raw_data_copy['datetime'] = pd.to_datetime(self._raw_data_copy['Date'], unit='ms')
        except Exception as e:
            print(f"[ERROR] Failed to convert datetime:")
            print(e)



    def get_raw_data(self) -> pd.DataFrame:
        return self._raw_data.copy()
    
    def as_candlesticks(self) -> List[candlestick]:
        json_data = loads(self._raw_data_copy.to_json(orient="split"))
        column_names = [col for col in json_data.get('columns', [])]
        data_rows = json_data['data']
       
        return [

            {
                "datetime": row[column_names.index('datetime')],
                "open": row[column_names.index('Open')],
                "close": row[column_names.index('Close')],
                "high": row[column_names.index('High')],
                "low": row[column_names.index('Low')],
                "index": i
            }
            for i, row in enumerate(data_rows)
        ]
    
    def as_single_ticks(self) -> List[tick]:
        json_data = loads(self._raw_data_copy.to_json(orient="split"))
        column_names = [col for col in json_data.get('columns', [])]
        data_rows = json_data['data']
       
        return [
            {
                "datetime": row[column_names.index('datetime')],
                "price": row[column_names.index('price_as_tick')],
                "buy_price": row[column_names.index('buy_price_as_tick')],
                "sell_price": row[column_names.index('sell_price_as_tick')],
                "index": i
            }
            for i, row in enumerate(data_rows)
        ]
    
    def get_pip_point(self) -> float:
        return self._pip_point
    
    def _get_pip_point(self, symbol: str) -> float:
                print(f"[DEBUG] Fetching pip point for symbol: {symbol}")
                return SYMBOLS[symbol].get("pip_point", 1.0)  # default to 1.0 if missing
    
