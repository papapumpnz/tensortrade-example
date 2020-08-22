from tensortrade.oms.wallets import Wallet, Portfolio
from tensortrade.oms.instruments import Quantity, USD, BTC, ETH, LTC

class BinancePortfolio():

    def __init__(self, exchange):
        self._exchange = exchange
        self._portfolio = self._setup()

    def _setup(self):

        # setup instruments. Must include base currency and your crypto
        instruments = [ Quantity(USD, 10000),
                        Quantity(BTC, 1) ]

        # setup wallet with instruments
        wallets = []
        for instrument in instruments:
            wallets.append(Wallet(self._exchange, instrument))

        # define portfolio with a wallet
        portfolio = Portfolio(
            base_instrument=USD,
            wallets=wallets
        )

        return portfolio

    @property
    def portfolio(self):
        return self._portfolio
