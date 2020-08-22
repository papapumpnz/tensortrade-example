import ta
import pandas as pd
from tensortrade.data.cdd import CryptoDataDownload
from tensortrade.feed.core import Stream, DataFeed, NameSpace


cdd = CryptoDataDownload()


def rsi(price: Stream[float], period: float) -> Stream[float]:
    """
    Relative strength index
    The relative strength index (RSI) is a momentum indicator used in technical analysis that measures the
    magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock or
    other asset
    :param price:
    :param period:
    :return:
    """
    r = price.diff()
    upside = r.clamp_min(0).abs()
    downside = r.clamp_max(0).abs()
    rs = upside.ewm(alpha=1 / period).mean() / downside.ewm(alpha=1 / period).mean()
    return 100*(1 - (1 + rs) ** -1)


def macd(price: Stream[float], fast: float, slow: float, signal: float) -> Stream[float]:
    """
    Moving Average Convergence Divergence
    This technical indicator is a tool that’s used to identify moving averages that are indicating a new trend,
    whether it’s bullish or bearish.
    :param price:
    :param fast:
    :param slow:
    :param signal:
    :return:
    """
    fm = price.ewm(span=fast, adjust=False).mean()
    sm = price.ewm(span=slow, adjust=False).mean()
    md = fm - sm
    signal = md - md.ewm(span=signal, adjust=False).mean()
    return signal


class DataManager():

    def __init__(self):
        self._data = self._fetch()
        self._stream = self._setup_stream()
        self._render_stream = self._setup_render_stream()

    def _fetch(self):
        """
        Fetches raw price data from https://www.cryptodatadownload.com/ from Binance exchange
        :return: Pandas.DataFrame
        """
        # get binance data
        binance_data = pd.concat([
            cdd.fetch("Binance", "USDT", "BTC", "1h")
        ], axis=1)

        # ta.add_all_ta_features(
        #     binance_data,
        #     **{k: k for k in ['open', 'high', 'low', 'close', 'volume']},
        #     fillna=True
        # )

        return binance_data

    def _setup_stream(self):
        """
        Sets up data stream with indicators and close
        :return: tensortrade.feed.core.DataFeed
        """

        features = []
        for c in self._data.columns[1:]:
            s = Stream.source(list(self._data[c]), dtype="float").rename(self._data[c].name)
            features += [s]

        cp = Stream.select(features, lambda s: s.name == "close")

        features = [
            cp.log().diff().rename("lr"),
            rsi(cp, period=20).rename("rsi"),
            macd(cp, fast=10, slow=50, signal=5).rename("macd")
        ]

        feed = DataFeed(features)
        feed.compile()

        return feed

    def _setup_render_stream(self):
        """
        Sets up indicator data stream for renderers with OHLC data
        :return: tensortrade.feed.core.DataFeed
        """
        renderer_feed = DataFeed([
            Stream.source(list(self._data["date"])).rename("date"),
            Stream.source(list(self._data["open"]), dtype="float").rename("open"),
            Stream.source(list(self._data["high"]), dtype="float").rename("high"),
            Stream.source(list(self._data["low"]), dtype="float").rename("low"),
            Stream.source(list(self._data["close"]), dtype="float").rename("close"),
            Stream.source(list(self._data["volume"]), dtype="float").rename("volume")
        ])

        renderer_feed.compile()

        return renderer_feed

    @property
    def data(self):
        """
        Returns raw data in OHLC column format
        :return: Pandas.DataFrame
        """
        return self._data

    @property
    def stream(self):
        """
        Returns data feed stream
        :return: tensortrade.feed.core.Stream
        """
        return self._stream

    @property
    def renderer_stream(self):
        """
        Returns raw data stream for renders
        :return: tensortrade.feed.core.DataFeed
        """
        return self._render_stream
