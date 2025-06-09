# List of common ticker symbols for financial instruments

SYMBOLS = {
    "^IXIC": {"id": "^IXIC", "description": "NASDAQ Composite", "pip_point": 1},
    "^GSPC": {"id": "^GSPC", "description": "S&P 500", "pip_point": 1},
    "^DJI": {"id": "^DJI", "description": "Dow Jones Industrial Average", "pip_point": 1},
    "^RUT": {"id": "^RUT", "description": "Russell 2000", "pip_point": 1},

    "EURUSD=X": {"id": "EURUSD=X", "description": "Euro to USD", "pip_point": 0.0001},
    "GBPUSD=X": {"id": "GBPUSD=X", "description": "British Pound to USD", "pip_point": 0.0001},
    "JPY=X": {"id": "JPY=X", "description": "USD to Japanese Yen", "pip_point": 0.01},
    "AUDUSD=X": {"id": "AUDUSD=X", "description": "Australian Dollar to USD", "pip_point": 0.0001},
    "USDCAD=X": {"id": "USDCAD=X", "description": "USD to Canadian Dollar", "pip_point": 0.0001},

    "GC=F": {"id": "GC=F", "description": "Gold Futures", "pip_point": 1.0},
    "SI=F": {"id": "SI=F", "description": "Silver Futures", "pip_point": 0.01},
    "CL=F": {"id": "CL=F", "description": "Crude Oil Futures", "pip_point": 0.001},

    "BTC-USD": {"id": "BTC-USD", "description": "Bitcoin to USD", "pip_point": 1 },
    "ETH-USD": {"id": "ETH-USD", "description": "Ethereum to USD", "pip_point": 1 },

    "SPY": {"id": "SPY", "description": "S&P 500 ETF", "pip_point": 0.01},
    "VTI": {"id": "VTI", "description": "Vanguard Total Stock Market ETF", "pip_point": 0.01},
    "QQQ": {"id": "QQQ", "description": "NASDAQ 100 ETF", "pip_point": 0.01},

    "AAPL": {"id": "AAPL", "description": "Apple Inc.", "pip_point": 0.01},
    "AMZN": {"id": "AMZN", "description": "Amazon", "pip_point": 0.01},
    "GOOGL": {"id": "GOOGL", "description": "Google", "pip_point": 0.01},
    "TSLA": {"id": "TSLA", "description": "Tesla Inc.", "pip_point": 0.01},
}