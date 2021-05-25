import pandas as pd
import numpy as np
import warnings
import time
import datetime as dt
import datetime
import matplotlib.pyplot as plt
from datetime import timedelta

warnings.filterwarnings('ignore')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

a = pd.read_html('https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters')

# Pull every df with an odd numbered indice out of table 'a'
n = 1
dflist = []
while n < len(a):  
    b = a[n].copy()
    dflist.append(b)
    n = n + 2
   
dfm = pd.concat(dflist)[['Name', 'DOB (YYYY-MM-DD)', 'From', 'Height', 'No.', 'Pos.',
       'Weight']]

nameset = list(dfm['Name'])


l = []

# Parse firstname,lastname by comma; keep only last name
for name in nameset:
    name2 = str(name)
    splitname = name2.split(',')
    l.append(splitname)

# Remove NaN values from any errors in data
for fl in l:
    if (len(fl) != 2) | fl == ['nan']:
        l.remove(fl)
    l.remove(l[-1])

iclist = []
# Add 'itch'es to new list
for fl in l:
    if (fl[0][-2:] == 'ić') | (fl[0][-2:] == 'ic'):
        iclist.append(fl)

print(iclist)
