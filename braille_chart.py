from plotille import Figure
from requests import get
from json import dump, load
from os import path
from time import time

timerange = "30"
interval = ""
filename = timerange + "range_" + interval + "interval.json"
if not path.isfile(filename) or (time() - path.getmtime(filename)) / 60 > 15:
    print("fetching")
    url = "https://bitcoincharts.com/charts/chart.json?m=bitstampUSD&SubmitButton=Draw&r={0}&i={1}".format(timerange,
                                                                                                           interval)
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
fig.set_x_limits(min_=0, max_=len(weighted))
fig.set_y_limits(min_=min(weighted), max_=max(weighted))
fig.color_mode = 'byte'
fig.plot([i for i in range(len(weighted))], weighted, lc=2, label="test")
print(fig.show(legend=True))
print('Data provided by bitcoincharts [{0}]'.format("http://bitcoincharts.com/"))
print('Last Updated {:.2} minutes ago'.format((time() - path.getmtime(filename)) / 60))
