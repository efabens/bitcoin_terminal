from plotille import Figure
from requests import get
from json import dump, load
from os import path
from time import time
from sys import argv


def create_chart(scriptpath):
    timerange = "60"
    interval = ""
    filename = scriptpath + timerange + "range_" + interval + "interval.json"
    if not path.isfile(filename) or (time() - path.getmtime(filename)) / 60 > 15:
        print("fetching")
        url = "https://bitcoincharts.com/charts/chart.json?m=bitstampUSD&SubmitButton=Draw&r={0}&i={1}"\
            .format(timerange, interval)
        with open(filename, "w") as file:
            dump(get(url).json(), file)
    else:
        print("loading cache")
    with open(filename, "r") as file:
        response = load(file)

    zipped = list(zip(*response))
    timestamps = zipped[0]
    weighted = zipped[7]

    fig = Figure()
    fig.width = 80
    fig.height = 10
    fig.x_axis_round = 2
    fig.set_x_limits(min_=min(timestamps), max_=max(timestamps))
    fig.set_y_limits(min_=min(weighted), max_=max(weighted))
    fig.y_label = "USD/BTC"
    fig.color_mode = 'byte'
    fig.plot(timestamps, weighted, lc=2, label="Bitcoin price")
    print(fig.show(legend=True))
    print('Data provided by bitcoincharts [{0}]'.format("http://bitcoincharts.com/"))
    print('Last Updated {:.2} minutes ago'.format((time() - path.getmtime(filename)) / 60))

if __name__ == '__main__':
    filepath = path.dirname(argv[0])
    if len(filepath) is not 0:
        filepath = filepath + "/"
    create_chart(filepath)
