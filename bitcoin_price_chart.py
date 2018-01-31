from argparse import ArgumentParser

from plotille import Figure
from requests import get
from json import dump, load
from os import path
from time import time
from sys import argv
from math import log, exp
from datetime import datetime


def create_chart(scriptpath, args):
    timerange = str(args.dayrange)
    interval = ""
    filename = scriptpath + timerange + "range_" + interval + "interval.json"
    if not path.isfile(filename) or (time() - path.getmtime(filename)) / 60 > 15 or args.force:
        url = "https://bitcoincharts.com/charts/chart.json?m=bitstampUSD&SubmitButton=Draw&r={0}&i={1}"\
            .format(timerange, interval)
        with open(filename, "w") as file:
            dump(get(url).json(), file)
    with open(filename, "r") as file:
        response = load(file)

    zipped = list(zip(*response))
    timestamps = zipped[0]
    weighted = zipped[7]
    print('Current price: ${:,.2f}'.format(weighted[-1]))
    if args.log:
        weighted = [log(i) for i in weighted]

    fig = Figure()
    fig.width = int(args.width)
    fig.height = int(args.height)
    fig.x_axis_round = 2
    fig.set_x_limits(min_=min(timestamps), max_=max(timestamps))
    fig.set_y_limits(min_=min(weighted), max_=max(weighted))
    fig.y_label = "USD/BTC"
    fig.color_mode = 'byte'
    fig.y_axis_transform = lambda x: "${:,.2f}".format(x)
    if args.log:
        fig.y_axis_transform = lambda x: "${:,.2f}".format(exp(x))
    fig.x_axis_transform = lambda x: '{:%m-%d-%y}'.format(datetime.fromtimestamp(x))
    fig.plot(timestamps, weighted, lc=2, label="Bitcoin price")

    print(fig.show(legend=True))
    print('Data provided by bitcoincharts [{0}]'.format("http://bitcoincharts.com/"))
    print('Last Updated {:.2} minutes ago'.format((time() - path.getmtime(filename)) / 60))

if __name__ == '__main__':
    filepath = path.dirname(argv[0])
    if len(filepath) is not 0:
        filepath = filepath + "/"
    parser = ArgumentParser(
        description='plots the historic price of bitcoin')
    parser.add_argument(
        '-r', '--range', dest='dayrange', default=30, help="Sets the number of days to go back for data")
    parser.add_argument(
        '-l', '--log', dest='log', action='store_true', help="Changes the scale to the log of the price")
    parser.add_argument('-w', '--width', dest='width', default=80, help="Sets the width of the chart")
    parser.add_argument('-t', '--height', dest='height', default=15, help="Sets the height of the chart")
    parser.add_argument(
        '-f', '--force', dest='force', action='store_true',
        help="If used forces a re-download of data. Data automatically updates if greater than 15 minutes old. "
             "This is not recommended to be used")
    args = parser.parse_args()

    create_chart(filepath, args)


