# Inspiration from: https://medium.com/swlh/5-simple-ways-to-calculate-customer-lifetime-value-5f49b1a12723

import pandas as pd
import datetime
import warnings
import math
import sys
import numpy as np
warnings.filterwarnings('ignore')

# This Method Calculates ARPU = (Total Revenue) / (Number of Customers for a chosen Time Period)
# ARPU = Average Revenue per User

def method1(clean_set_base, start_ym, end_ym):
    '''
    Returns ARPU for a chosen time period
    '''

    dfs = clean_set_base.copy()
    dfs.CustomerKey = dfs.CustomerKey.astype(str)
    dfs.Postdate = pd.to_datetime(dfs.Postdate).dt.normalize()
    dfs['ym'] = list(zip(dfs.Postdate.dt.year, dfs.Postdate.dt.month))

    # Number of Customers for Chosen Period
    dfs = dfs[(dfs.ym >= start_ym) & (dfs.ym <= end_ym)]
    numberOfCustomers = len(dfs.CustomerKey.unique().tolist())

    # Total Revenue
    totalRevenue = dfs['New Settled Amount'].sum()

    ARPU = totalRevenue/numberOfCustomers

    return ARPU

# Example Usage
method1(<settled data df>, (2018,1), (2018,12))

# Expand above usage for ARPU's over full year by month
x = 1
while x <= 12:
    print('ARPU From (2018, {}) to (2018, 12): '.format(x), '$', method1(clean_setb, (2018, x), (2018, 12)).round(2))
    x += 1
