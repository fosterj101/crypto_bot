# crypto_bot
starting with historical data

first attempt at a crypto bot using ccxt

## exchange used
Think about using binance, need to do more research

## pandas dataframe

## strategy
Markowitz Model

RSI, moving average, 

Dollar Cost Averaging (DCA)

METHODS TO EXPLORE
Parabolic SAR, Bollinger Bands, MACD, Momentum, Awesome Oscillator,
Average Directional Index, Commondity Channel Index, Stochastic, Relative Strength Index,
Simple & Exponential Moving Averages


## backtesting
[https://github.com/quantopian/pyfolio]


# considerations
- price fluctuation mid trade
    - solution: save order transaction number, and if order doesnt go through after some time frame, cancel it
- limit orders are friends
    - make limit order so you don't lose money on rapid price changes
    - possible solution, give price some "wiggle room" have it buy at certain amount below desired price
    - would make less trades but would avoid some shitty buys

- understand how precise orders can be

- dont trade to rapidly with the server

- need to check for lost connection
    - having save states to check for blank data and pause program if seen

- have bot send me texts
    - approving orders
    - seeing results

- Use static analysis
    - not sure what this is but use PyLint and PyFlakes to catch bugs?



- have table with 24h highs and lows

- learn about fees

# help

discuss.hackingthemarket.com