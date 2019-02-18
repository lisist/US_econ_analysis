from fed import *
from us_econ import *
from data_modifier import *
import datetime as dt


def plot_with_rec(data, start, end):
    recession_period = us_recession(start, end)
    fig, ax1 = plt.subplots()
    ax1.plot(data,color='black')
    range_list =[]
    for i,j in recession_period.iterrows():
        range_list.append((j['start'],j['end']))

    for (start,end) in range_list:
        plt.axvspan(start, end, color='grey',alpha=0.3)


def curve_invert_corp_profit():
    start = dt.datetime(1980,1,1)
    end = dt.datetime(2018,12,31)

    corp_prof = corporate_prof_iva_cca(start,end)
    us_spread = sp2y10y(start,end)

    us_spread = us_spread.groupby(pd.Grouper(freq='M')).last()/10

    fig, ax1 = plt.subplots()

    ax1.plot(us_spread,color='black')
    ax1.plot(yoy(corp_prof,freq='q'),color='grey')
    ax1.axhline(0,ls='--')

    fig.tight_layout()


def ism_pmi_recession(start,end):

    pmi = ism_pmi(start,end)
    plot_with_rec(pmi,start,end)

    return pmi



def hh_debt_to_dispo_income(start,end):
    debt = hh_debt(start,end)
    income = disposable_income(start,end)

    debt_income = pd.merge(debt,income,on='DATE')

    data = debt_income['CMDEBT']/debt_income['DSPI']

    plot_with_rec(yoy(data,freq='q'),start,end)
    plt.title('House hold debt to disposable income YoY')
    plt.axhline(y=0,color='green',linestyle='--')

    plt.show()


def hh_debt_service_recession(start, end):
    debt_service = hh_debt_service_ratio(start,end)
    print(debt_service.tail())
    plot_with_rec(debt_service,start,end)

    plt.title("US HH_Debt Service Ratio %")

    plt.show()


def capacity_utilization_recession(start, end):
    cap_data = capacity_utilization(start,end)
    print(cap_data.mean()['TCU'])
    plot_with_rec(cap_data,start,end)
    plt.axhline(y=cap_data.mean()['TCU'],linestyle='--')
    plt.show()


start = dt.date(1980,1,1)
end = dt.date(2019,1,31)

capacity_utilization_recession(start,end)



# plt.plot(us_spread)
# plt.plot(yoy(corp_prof,freq='q'),'-.')
# plt.xlabel('date')
# plt.ylabel('yoy%')
# vals = plt.get_yticks()
# plt.set_xlim([start,end+dt.timedelta(weeks=30)])
# plt.set_yticklabels(['{:,.2%'.format(x) for x in vals])
# ax1.subplot().set_xlabel('date')
# ax1.subplot().set_ylabel('mom%')
# ax1.set_xlabel('date')
# vals = ax1.get_yticks()
# ax1.set_xlim([start,end+dt.timedelta(weeks=30)])
#
# ax1.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
