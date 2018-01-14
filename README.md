Each json response is a list of lists.

Each element of the top level list represents a trading period as defined in the query params with value `i`.
the number of elements in the list is based of of the query param `r`.

The `r` value is days back as an integer
the `i` value is interval period and appears to be enumerated values that are allowed include but may not be limited too (additionally `i` can be left blank and it will auto scale, but the autoscaling size is not reported):
fill this in

each element of the top level list features 8 elements (as of 1/13/2018 at 5PM PST) Those elements represent
0: timestamp in epoch seconds
1: Open
2: High
3: Low
4: Close
5: Volume (BTC)
6: Volume (Currency)
7: Weighted Price