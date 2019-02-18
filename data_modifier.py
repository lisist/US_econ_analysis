## Data modifier
## Ver 0.1 as of Feb. 2018

import pandas as pd

def yoy(data, freq='m'):
    ## Calculate Year over Year changes
    ## Data type is dataframe
    if freq == 'm' :
        count = 12
    elif freq == 'q':
        count = 4
    elif freq == 'w':
        count = 52

    yoy_ch = (data - data.shift(count)) / data.shift(count)
    yoy_ch.dropna(axis=0, inplace=True)

    return yoy_ch

def qoq(data, freq='m'):
    ## Calculate Quarter over Quarter
    ## Data type is dataframe
    if freq == 'm':
        count = 4
    elif freq == 'q':
        count = 1
    elif freq == 'w':
        count = 12

    mom_ch = (data - data.shift(count)) / data.shift(count)
    mom_ch.dropna(axis=0, inplace=True)

    return mom_ch

def mom(data, freq='m'):
    ## Calculate Month over Month
    ## Data type is dataframe
    if freq == 'm' :
        count = 1
    elif freq == 'w':
        count = 4

    mom_ch = (data - data.shift(count)) / data.shift(count)
    mom_ch.dropna(axis=0, inplace=True)

    return mom_ch

def monthly(data):
    monthly_data = data.groupby('month').first()

    return monthly_data

