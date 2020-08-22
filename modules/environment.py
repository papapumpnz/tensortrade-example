import tensortrade.env.default as default
from modules import renderers as render


class Environment():

    def __init__(self, portfolio, data_stream, renderer_stream):
        self._portfolio = portfolio
        self._data_stream = data_stream
        self._renderer_stream = renderer_stream
        self._environment = self._setup()

    def _setup(self):
        env = default.create(
            portfolio=self._portfolio,
            action_scheme="managed-risk",
            reward_scheme="risk-adjusted",
            feed=self._data_stream,
            renderer_feed=self._renderer_stream,
            renderer=render.file_logger,
            window_size=20
        )

        return env

    @property
    def environment(self):
        return self._environment