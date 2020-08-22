from tensortrade.env.default.renderers import PlotlyTradingChart, FileLogger, ScreenLogger

chart_renderer = PlotlyTradingChart(
    display=True,  # show the chart on screen (default)
    height=800,  # affects both displayed and saved file height. None for 100% height.
    save_format="html",  # save the chart to an HTML file
    auto_open_html=True,  # open the saved HTML chart in a new browser tab
    path="../charts"
)

file_logger = FileLogger(
    filename="example.log",  # omit or None for automatic file name
    path="../training_logs"  # create a new directory if doesn't exist, None for no directory
)

screen_logger = ScreenLogger(date_format="%Y-%m-%d %H:%M:%S %p")