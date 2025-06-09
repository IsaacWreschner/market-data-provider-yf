class tick:
    """
    Class to represent a tick in the market data.
    """
    def __init__(self, datetime: str, price: float, buy_price: float, sell_price: float, index: int):
        self.datetime = datetime
        self.price = price
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.index = index
    
    def __repr__(self):
        return f"Tick(datetime={self.datetime}, price={self.price}, buy_price={self.buy_price}, sell_price={self.sell_price})"