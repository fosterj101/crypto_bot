import ccxt
import pandas as pd

data = pd.DataFrame(data=None, columns=None)


class coin:
    purchasedPrice = 0.0
    numHeld = 0.0
    numBought = 0.0
    name = ""
    lastBuyOrder = ""
    timeBought = ""

    def __init__(self, name=""):
        print("Creating coin " + name)
        self.name = name
        self.purchasedPrice = 0.0
        self.numHeld = 0.0
        self.numBought = 0.0
        self.lastBuyOrderID = ""
        self.timeBought = ""