

Each json response is a list of lists.

Each element of the top level list represents a trading period as defined in the query params with value `i`.
the number of elements in the list is based of of the query param `r`.

The `r` value is days back as an integer
the `i` value is interval period and appears to be enumerated values that are allowed include but may not be limited too (additionally `i` can be left blank and it will auto scale, but the autoscaling size is not reported):
* `30-min`
* `hourly`
* `daily`
* `2-hour`

each element of the top level list features 8 elements (as of 1/13/2018 at 5PM PST) Those elements represent
1. timestamp in epoch seconds
1. Open
1. High
1. Low
1. Close
1. Volume (BTC)
1. Volume (Currency)
1. Weighted Price

The plotting library used is a custom fork of [plotille](https://github.com/tammoippen/plotille). The modifications make the axis values more appropriate for the data type. Including reducing the number of decimal points on the y axis and making the x axis show dates