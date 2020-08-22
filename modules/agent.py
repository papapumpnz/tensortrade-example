from tensortrade.agents import DQNAgent

class Agent():

    def __init__(self, environment):
        self._agent = DQNAgent(environment)


    def train(self, steps, episodes, save_path='agents/', render_interval=10):
        return self._agent.train(n_steps=steps, n_episodes=episodes, save_path=save_path, render_interval=render_interval)

    @property
    def agent(self):
        return self._agent