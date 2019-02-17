import datetime as dt
import pandas_datareader as web
import pandas as pd

def fdtr(start_date, end_date):
    fftr_ex = web.DataReader('DFEDTAR', 'fred', start_date, end_date)
    fftr = web.DataReader('DFEDTARU', 'fred', start_date, end_date)  ## upper limit of fed fund target rate

    fftr.rename(columns={'DFEDTARU': 'FFTR'}, inplace=True)
    fftr_ex.rename(columns={'DFEDTAR': 'FFTR'}, inplace=True)

    fdtr = pd.concat([fftr_ex, fftr])

    return fdtr

def fdasset(start_date, end_date):
    asset = web.DataReader('WALCL','fred',start_date, end_date)

    return asset

def sp2y10y(start_date, end_date):
    spread = web.DataReader('T10Y2Y','fred',start_date, end_date)

    return spread

def ip(start_date, end_date):
    industrial_production = web.DataReader('INDPRO','fred',start_date,end_date)

    return industrial_production

def yoych(data,freq = 'm'):
    ## Calculate Year over Year changes
    
    yoy = (data-data.shift(12))/data.shift(12)
    yoy.dropna(axis=0,inplace=True)

    return yoy
