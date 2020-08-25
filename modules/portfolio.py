from tensortrade.oms.wallets import Wallet, Portfolio
from tensortrade.oms.instruments import Quantity, USD, BTC, ETH, LTC

def BinancePortfolio(exchange):

    # setup instruments. Must include base currency and your crypto
    instruments = [ Quantity(USD, 10000),
                    Quantity(BTC, 1) ]

    # setup wallet with instruments
    wallets = []
    for instrument in instruments:
        wallets.append(Wallet(exchange, instrument))

    # define portfolio with a wallet
    portfolio = Portfolio(
        base_instrument=USD,
        wallets=wallets
    )

    return portfolio

