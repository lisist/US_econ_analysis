import datetime as dt
import pandas_datareader as web
import pandas as pd
from data_modifier import *
import matplotlib.pyplot as plt
import quandl

## you need quandl API key
quandl.ApiConfig.api_key = "Your api key"

def us_recession(start, end):
    recession = pd.read_csv('us_recession.csv')

    recession_start = recession['Peak']
    recession_end = recession['Trough']

    recession_start_date =[]
    recession_end_date = []

    for i in recession_start:
        recession_start_year = pd.to_numeric(i[0:4])
        recession_start_month = pd.to_numeric(i[-2:])
        recession_start_date.append(dt.date(recession_start_year,recession_start_month,15))

    for j in recession_end:
        recession_end_year = pd.to_numeric(j[0:4])
        recession_end_month = pd.to_numeric(j[-2:])
        recession_end_date.append(dt.date(recession_end_year,recession_end_month,15))

    recession_period = pd.DataFrame([recession_start_date,recession_end_date],index=['start','end']).transpose()

    recession_period = recession_period[(recession_period['start'] > start) & (recession_period['end'] < end) ]
    recession_period.reset_index(drop=True, inplace=True)

    return recession_period



def retail_sales(start,end):
    rt_sales = web.DataReader('RSXFS','fred',start,end)

    return rt_sales



def retail_sales_xauto(start,end):
    rt_sales = web.DataReader('RSFSXMV','fred',start,end)

    return rt_sales



def corporate_prof_iva_cca(start,end):
    cor_prof = web.DataReader('CPATAX','fred',start,end)

    return cor_prof



def ism_pmi(start,end):
    ism = quandl.get("ISM/MAN_PMI",start_date=start,end_date=end)

    return ism
