# Inspiration from: https://medium.com/swlh/5-simple-ways-to-calculate-customer-lifetime-value-5f49b1a12723

import pandas as pd
import datetime
import warnings
import math
import sys
import numpy as np
warnings.filterwarnings('ignore')

# This method calculates Average Revenue per Cohort rather than User/Customer level
# Cohort = a group of customers with similar characteristics
# In this usage we define a cohort by customers who made their first purchase during the same month

def cohort_signups_pyramid():
    '''Calculates and Computes a Cohort Pyramid Table for # of Signups by Month'''
    def do_function(yearmon, dfse, dfad, dfsu):

        ck_list = []
        ck_dict = {}

        dfse = dfse[dfse.ym >=  yearmon]

        signups = set(dfsu[dfsu.ym == yearmon].CustomerKey)
        adds = set(dfad[dfad.ym == yearmon].CustomerKey)
        settleds = set(dfse[dfse.ym == yearmon].CustomerKey)
        start_ck = signups
            # print('Initial for ', yearmon, ': ', len(start_ck))
        ck_list.append(len(start_ck))
        ck_dict[yearmon] = len(start_ck)

        dfse = dfse[dfse.ym > yearmon]
        ymlist = list(dfse.ym.unique())
        for ym in ymlist:
            settleds = set(dfse[dfse.ym == ym].CustomerKey)
            next_ck = start_ck.intersection(settleds)
            ck_list.append(len(next_ck))
            ck_dict[ym] = len(next_ck)

        df = pd.DataFrame(ck_dict, index=['a'], columns=list(ck_dict.keys()))
        return df

    global dfsettled3, dfca3, dfcs3

    ymlist = list(dfsettled3.ym.unique())
    dflist = []
    for ym in ymlist:
        codf = do_function(ym, dfsettled3, dfca3, dfcs3)
        dflist.append(codf)

    df_all = pd.concat(dflist)

    return df_all

def method2b_rev():

    def do_function(yearmon, dfse, dfad, dfsu):

        ck_list = []
        rev_dict = {}
        dfse = dfse[dfse.ym >=  yearmon]

        signups = set(dfsu[dfsu.ym == yearmon].CustomerKey)
        start_ck = signups
        print('Initial for ', yearmon, ': ', len(start_ck))
        num_signups = len(start_ck)

        rev = dfse[dfse.CustomerKey.isin(start_ck)]['New Settled Amount'].sum()
        rev_dict[yearmon] = rev

        dfse = dfse[dfse.ym > yearmon]
        ymlist = list(dfse.ym.unique())
        for ym in ymlist:
            settleds = set(dfse[dfse.ym == ym].CustomerKey)
            next_ck = start_ck.intersection(settleds)
            rev = dfse[dfse.CustomerKey.isin(next_ck)]['New Settled Amount'].sum()
            rev_dict[ym] = rev

        df = pd.DataFrame(rev_dict, index=['Revenue:'], columns=list(rev_dict.keys()))
        return df, num_signups

    global dfsettled3, dfca3, dfcs3

    ymlist = list(dfsettled3.ym.sort_values().unique())
    dflist = []
    sulist = []
    for ym in ymlist:
        codf, nsignups = do_function(ym, dfsettled3, dfca3, dfcs3)
        dflist.append(codf)
        sulist.append(nsignups)

    df_all = pd.concat(dflist)

    return df_all, sulist, ymlist

def make_neat(a,b,c):
    '''Cleans and Formats the table output by the above function
    into a deliverable ready form'''
    r = a.copy().reset_index().fillna(0).round(2)
    s = b.copy()
    m = c.copy()

    newcol = {'Signups':s, 'Month':m}
    attach = pd.DataFrame(newcol)
    r.insert(0, 'Signups', s, True)
    r.insert(0, 'YYYY-MM', m, True)

    wii = r.columns
    newcols = []
    for col in wii:
        newcol = str(col[0])+'-'+str(col[1])
        newcols.append(newcol)

    r.columns = newcols
    if 'YYYY-MM-' in r:
        r.rename(columns=
            {'YYYY-MM-':'MMM-YY',
            'Signups-':'Signups:',
            'index-':'dropthiscolumn',
            '2019-1':'Jan-19',
            '2019-2':'Feb-19',
            '2019-3':'Mar-19',
            '2019-4':'Apr-19',
            '2019-5':'May-19',
            '2019-6':'Jun-19',
            '2019-7':'Jul-19',
            '2019-8':'Aug-19',
            '2019-9':'Sep-19',
            '2019-10':'Oct-19',
            '2019-11':'Nov-19',
            '2019-12':'Dec-19',
            '2020-1':'Jan-20',
            '2020-2':'Feb-20',
            '2020-3':'Mar-20'}, inplace=True)

    return r[['MMM-YY', 'Signups:', 'Jan-19', 'Feb-19', 'Mar-19',
           'Apr-19', 'May-19', 'Jun-19', 'Jul-19', 'Aug-19',
           'Sep-19', 'Oct-19', 'Nov-19', 'Dec-19', 'Jan-20',
           'Feb-20', 'Mar-20']]

# example usage for cohort signups
cohort_signups_pyramid()

# cohort usage for cohort / lifetime revenue
a, b, c = method2b_rev()
print(a)

# example usage of make_neat function
make_neat(a)
