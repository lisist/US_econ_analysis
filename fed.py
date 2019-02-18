import datetime as dt
import pandas_datareader as web
import pandas as pd
from data_modifier import *
import matplotlib.pyplot as plt

def fdtr(start_date, end_date):
    fftr_ex = web.DataReader('DFEDTAR', 'fred', start_date, end_date)
    fftr = web.DataReader('DFEDTARU', 'fred', start_date, end_date)  ## upper limit of fed fund target rate

    fftr.rename(columns={'DFEDTARU': 'FFTR'}, inplace=True)
    fftr_ex.rename(columns={'DFEDTAR': 'FFTR'}, inplace=True)

    fdtr = pd.concat([fftr_ex, fftr])

    return fdtr


def fdasset(start_date, end_date):
    asset = web.DataReader('WALCL', 'fred', start_date, end_date)

    return asset


def sp2y10y(start_date, end_date):
    spread = web.DataReader('T10Y2Y', 'fred', start_date, end_date)

    return spread


def ip(start_date, end_date):
    industrial_production = web.DataReader('INDPRO', 'fred', start_date, end_date)

    return industrial_production


def hh_debt(start_date,end_date):
    household_debt = web.DataReader('CMDEBT','fred',start_date,end_date)

    return household_debt

def disposable_income(start_date, end_date):
    dis_income = web.DataReader('DSPI','fred',start_date,end_date)

    return dis_income

def hh_debt_service_ratio(start_date,end_date):
    # Household debt service payment as a percent of disposable income
    # Quarterly

    debt_service = web.DataReader('TDSP','fred',start_date,end_date)

    return debt_service

def capacity_utilization(start_date,end_date):
    # Capacity utilization tracks the extent to which the installed productive capacity of a country is being used
    # in the production of goods and services.
    # monthly

    __capacity_utilization = web.DataReader('TCU','fred',start_date,end_date)

    return __capacity_utilization
