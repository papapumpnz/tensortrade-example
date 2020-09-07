from modules.data_manager import DataManager
from modules.exchange import BinanceExchange
from modules.portfolio import BinancePortfolio
from modules.environment import Environment
from modules.agent import Agent
from modules.tensorflow_fix import memory_fix, memory_hard_fix

import matplotlib.pyplot as plt

# https://www.tensortrade.org/en/latest/


def run():

    # uncomment these if you want
    #memory_fix()
    #memory_hard_fix()

    # setup data feed
    dm = DataManager()

    # for _ in range(10):
    #     print(dm.renderer_stream.next())

    # setup exchange. Needs raw data
    binance_exchange = BinanceExchange(data=dm.data)

    # setup portfolio
    binance_portfolio = BinancePortfolio(exchange=binance_exchange)

    # setup environment. Needs data feed stream
    env = Environment(portfolio=binance_portfolio, data_stream=dm.stream, renderer_stream=dm.renderer_stream)

    # for _ in range(10):
    #     print(env.observer.feed.next())

    # setup agent
    agent = Agent(environment=env)

    # train agent
    print(agent.train(steps=100, episodes=4, render_interval=10))


    # show plots of performance
    a = binance_portfolio.performance.plot()
    plt.show()
    b = binance_portfolio.performance.net_worth.plot()
    plt.show()

if __name__ == '__main__':
    run()