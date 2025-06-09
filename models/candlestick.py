class candlestick:
    def __init__(self, datetime, open, high, low, close):
        self.datetime = datetime
        self.open = open
        self.high = high
        self.low = low
        self.close = close

    def __repr__(self):
        return f"Candle(open={self.open}, high={self.high}, low={self.low}, close={self.close})"