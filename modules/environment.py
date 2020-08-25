import tensortrade.env.default as default
from modules import renderers as render


def Environment(portfolio, data_stream, renderer_stream):

    env = default.create(
        portfolio=portfolio,
        action_scheme="managed-risk",
        reward_scheme="risk-adjusted",
        feed=data_stream,
        renderer_feed=renderer_stream,
        renderer=render.file_logger,
        window_size=20
    )

    return env