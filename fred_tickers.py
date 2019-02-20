### This code is for scrapping Fred economic tickers for further economic analysis

import requests
import bs4 as bs
import pandas as pd

import matplotlib.pyplot as plt
import pandas_datareader as web
import datetime as dt
from data_modifier import *

def read_tickers(page = 30):
    names = []
    links = []

    for page in range(1,page+1):
        resp = requests.get('https://fred.stlouisfed.org/tags/series?t=&et=&pageID='+str(page))
        soup = bs.BeautifulSoup(resp.text)
        table = soup.find('table',{'id':'series-pager'})

        for rows in table.findAll('tr',{'class':'series-pager-title'})[0:]:
            link = rows.find('a')
            link = link.get('href')
            link = link.strip('/series/')
            links.append(link)

            if type(rows) is not bs.element.NavigableString:
                name=rows.text
                name = name.strip('\n')
                name = name.strip('\xa0')
                name = name.strip('\n\n\n\xa0 ')
                names.append(name)

    tickers = pd.DataFrame({'Name':names,'ticker':links})
    tickers.to_csv('fred_tickers.csv')

def search(quary):

    df = pd.read_csv('fred_tickers.csv',index_col=0)
    cf = (df['Name'].str.lower()).str.find(quary)
    name = df['Name'][cf!= -1]
    ticker = df['ticker'][cf != -1]

    tickers = pd.DataFrame({'Name':name,'ticker':ticker})
    return tickers

def plot_search_result(start, end, howmany = 10) :
    for i,j in result[0:howmany].iterrows():

        print(j[0])

        ticker_data = web.DataReader(j[1],'fred',start,end)
        try:
            ticker_data.plot(title=j[0])
        except:
            pass

    plt.show()


result = search('china')

start = dt.datetime(2010,1,1)
end = dt.datetime(2019,1,31)

plot_search_result(start,end,3)
