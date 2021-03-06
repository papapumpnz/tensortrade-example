from tensortrade.oms.exchanges import Exchange
from tensortrade.oms.services.execution.simulated import execute_order
from tensortrade.feed.core import Stream

"""
Exchanges determine the universe of tradable instruments within a trading environment, return observations to the 
environment on each time step, and execute trades made within the environment. There are two types of exchanges: live and simulated.
Live exchanges are implementations of Exchange backed by live pricing data and a live trade execution engine. 

For example, CCXTExchange is a live exchange, which is capable of returning pricing data and executing trades on 
hundreds of live cryptocurrency exchanges, such as Binance and Coinbase.
"""

def BinanceExchange(data):

    exchange = Exchange("binance", service=execute_order)(
        Stream.source(list(data['close']), dtype="float").rename("USD-BTC")
    )

    return exchange

