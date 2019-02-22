import pandas_datareader as web
import pandas as pd
import datetime as dt
from data_modifier import *
import matplotlib.pyplot as plt
import hub as hub
from us_econ import *
import os

def get_spx(start,end):
    df = web.DataReader('^GSPC','yahoo',start,end)

    df.to_csv("chart_stock_to_bond_data/spx.csv")
    return(df)

def get_ust10y(start,end):
    df = web.DataReader('DGS10','fred',start,end)

    df.to_csv("chart_stock_to_bond_data/ust10y.csv")
    return(df)

start = dt.datetime(1989,1,1)
end = dt.datetime(2019,2,19)

if not os.path.exists('chart_stock_to_bond_data'):
    os.makedirs('chart_stock_to_bond_data')
    print('have made dirs')

if not os.path.isfile('chart_stock_to_bond_data/spx.csv'):
    get_spx(start, end)
    print('spx.csv file created')

if not os.path.isfile('chart_stock_to_bond_data/ust10y.csv'):
    get_ust10y(start,end)
    print('ust10y file created')


### 기존 CSV 파일에서 Data 받기
spx = pd.read_csv('chart_stock_to_bond_data/spx.csv',parse_dates=True, index_col=0)
spx.drop(['High','Low','Volume','Open','Close'],axis=1,inplace=True)
ust10 = pd.read_csv('chart_stock_to_bond_data/ust10y.csv',parse_dates=True,index_col=0)


### 파일 업데이트 여부 체크
first_date = ust10.index[0]
length = ust10.index.__len__()
last_date = ust10.index[length-1]

if(start < first_date):
    df = web.DataReader('DGS10','fred',start,first_date)
    print(df)




ust10.index.names=['Date']





# print(type(spx['Date']))

# print(spx.head())
# print(ust10.head())
#
# print(spx.tail())
merged = pd.merge(spx,ust10,how='outer', on='Date')
merged.dropna(inplace=True)


merged  = merged.iloc[merged.reset_index().groupby(merged.index.to_period('M'))['Date'].idxmax()]
merged = merged.rename(columns={'Adj Close':'Spx','DGS10':'UST10'})


spx_index = pd.DataFrame((merged['Spx']/merged['Spx'][0]).values,index = merged.index,columns=['spx index']) ## spx indexation
ust_index_return = ((merged['UST10']-merged['UST10'].shift(1))*8/100+merged['UST10']/12/100)



a = 1
k = []

for i in ust_index_return[1:]:
    a = a*(1+i)
    k.append(a)

rgdp = web.DataReader('GDPC1','fred',start,end)
rgdp = yoy(rgdp,freq='q')


ust_index_return.dropna(inplace= True)

k = pd.DataFrame(k,index=ust_index_return.index,columns=['ust10y'])
stock_to_bond = (spx_index['spx index']/k['ust10y'])
stock_to_bond = yoy(stock_to_bond,freq='m')



fig, ax1 = plt.subplots()
lns1 = ax1.plot(stock_to_bond, color= 'black',label = 'stock_to_bond (LHS)')
ax2 = ax1.twinx()
lns2 = ax2.plot(rgdp, '--',color= 'grey',label = 'Real GDP YoY% (RHS)')
lns = lns1+lns2
labs = [l.get_label() for l in lns]
plt.legend(lns,labs,loc=0)
plt.title('Stock to bond ratio and US real GDP YoY%')


plt.show()


# hub.plot_with_rec(yoy_spx,start,end)
