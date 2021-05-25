import pandas as pd
import datetime
from datetime import timedelta
import math
import warnings
warnings.filterwarnings('ignore')
now = datetime.datetime.now()

def get_inputs():

    print('No Quotes Needed!')
    init_date = input('Date Input : ')

    n = int(input('Number of Brands affected : '))

    brand_list = []

    for i in range(n):
        brand =  input('Brand Input (one at a time): ')
        brand_list.append(brand)

    return init_date, brand_list

def est_loss(same_day):

    dfa = pd.read_csv('generic_data.csv') # csv for mainsnap
    dfa.Date = pd.to_datetime(dfa.Date).dt.normalize()
    dfa = dfa[dfa.Brand.isin(brand_list)]

    prior_days = []

    if same_day == True:

        for x in range(52):
            prior_date = pd.to_datetime(init_date) - timedelta(days=7*x)
            prior_days.append(prior_date)

        NoS_dict = {}

        for day in prior_days:
            nos = dfa[dfa.Date == day].Signups.sum()
            NoS_dict[str(day)[:-9]] = nos

        df = pd.DataFrame(NoS_dict.items(), columns = ['Date','Signups'])
        df.sort_values(by='Date', ascending=False, inplace=True)
        df_day = df.reset_index(drop=True).loc[:10]
        df_day['What?'] = 'Yes'
        return df_day

    else:

        for x in range(30):
            prior_date = pd.to_datetime(init_date) - timedelta(days=x)
            prior_days.append(prior_date)

        NoS_dict = {}

        for day in prior_days:
            nos = dfa[dfa.Date == day].Signups.sum()
            NoS_dict[str(day)[:-9]] = nos

        df = pd.DataFrame(NoS_dict.items(), columns = ['Date','Signups'])
        df.sort_values(by='Signups', ascending=False, inplace=True)
        df_rec = df.reset_index(drop=True).loc[:10]
        return df_rec

def avg(df):


    avg_signups = df.Signups.mean()
    main_signup = int(df[df.Date == init_date].Signups.sum())

    if 'What?' in list(df.columns):
        print('Average DoW vs {} Signups is {}'.format(init_date, avg_signups - main_signup))
        print(avg_signups)
        return avg_signups, main_signup

    else:
        print('Average Recent vs {} Signups is {}'.format(init_date, avg_signups - main_signup))
        print(avg_signups)
        return avg_signups, main_signup

def graph_day(df):

    import matplotlib.pyplot as plt
    import numpy as np

    x = list(df.Date)
    y = list(df.Signups.astype(int))

    fig, ax = plt.subplots()
    bar = ax.bar(x,y)

    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Signups')

    if 'What?' in list(df.columns):

        plt.title('Top 10 Mondays')
        plt.ylim((1000, 2000))
        bar[9].set_color('r')

    else:

        plt.title('Top 10 Most Recent Days')
        plt.ylim((1000,2000))
        bar[6].set_color('r')

    def autolabel(bar):
        for rect in bar:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(bar)
    plt.show()

def graph_rec(df):

    import matplotlib.pyplot as plt
    import numpy as np

    x = list(df.Date)
    y = list(df.Signups.astype(int))

    fig, ax = plt.subplots()
    bar = ax.bar(x,y)

    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Signups')

    if 'What?' in list(df.columns):
        plt.title('Top 10 Mondays')
        plt.ylim((0, 2000))
        bar[9].set_color('r')

    else:
        plt.title('Top 10 Most Recent Days')
        plt.ylim((0,2000))
        bar[6].set_color('r')

    def autolabel(bar):
        for rect in bar:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(bar)
    plt.show()

def get_yield():


    dfn = pd.read_csv('generic_data.csv') # CSV for net adds
    dfn.rename(columns = {'Cohort NA Date':'Date'}, inplace=True)
    dfn = dfn[dfn.Brand.isin(brand_list)]

    dfa = pd.read_csv('generic_data.csv') # CSV for clean adds
    dfa = dfa[dfa.Brand.isin(brand_list)]
    dfa.rename(columns = {'Service Start Date':'Date'}, inplace=True)
    print('Reading, Subsetting : COMPLETE')

    def ym(df):

        df.Date = pd.to_datetime(df.Date).dt.normalize()
        df['ym'] = list(zip(df.Date.dt.year, df.Date.dt.month))

    ym(dfa)
    ym(dfn)
    print("YM'ing : COMPLETE")

    dfa = dfa.groupby(['Brand','ym']).agg({'CustomerKey':'nunique'}).reset_index()
    dfa.columns = ['Brand','ym','Signups']

    dfn = dfn.groupby(['Brand','ym']).agg({'Net Adds':'sum'}).reset_index()

    df = dfa.merge(dfn, how='left', on=['Brand','ym'])
    df = df[(df.ym >= (2019,1)) & (df.ym < (now.year, now.month))]

    yieldy = df['Net Adds'] / df['Signups']
    yieldy = [round(x*100,2) for x in yieldy]

    df['Yield'] = yieldy
    print('Yield : GOT')

    yield_dict = {}
    for brand in brand_list:
        dft = df[df.Brand == brand]
        avg_yield = dft.Yield.mean()
        print('Average Yield for {} is {}'.format(brand, avg_yield))
        yield_dict[brand] = avg_yield

    print('DONE')

    return yield_dict

def construct_df():
    df = pd.DataFrame({'Missed Signups':'689',
                       'Avg Yield':'54.42%',
                       'Missed Net Adds':375,
                       'Avg ARPA':'18.90',
                       'Estimated 1 Year Loss':'$85,050'}, index=[0])
    return df


# Input date of outtage and brand(s) affected
init_date, brand_list = get_inputs()

# Input same day of week or not
df_day = est_loss(True)
df_rec = est_loss(False)
print(df_day, df_rec)

# Compute Average of KPIs over that day over past X weeks
rec_avg, main_signup = avg(df_rec)
day_avg, main_signup = avg(df_day)

# Graph top 10 day-of-the-week
graph_day(df_day)

# Graph top 10 most recent Days
graph_rec(df_rec)

# Calculate Yield
dft = get_yield()

# Create Report DataFrame
df = construct_df()
print(df)
