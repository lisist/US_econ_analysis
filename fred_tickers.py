### This code is for scrapping Fred economic tickers for further economic analysis

import requests
import bs4 as bs
import pandas as pd

names = []
links = []

for page in range(1,31):
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
