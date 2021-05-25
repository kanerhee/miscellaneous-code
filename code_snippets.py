import os
import shutil

# Get the base path of Python working directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('Helper Functions.ipynb')))
print('Base Directory: ', BASE_DIR)

# Check current working directory
CURR_DIR = os.path.dirname(os.path.realpath('Helper Functions.ipynb'))
print('Current Directory: ', CURR_DIR)

# Check current working directory (II.)
CURR_DIR = os.getcwd()
print('Current Directory: ', CURR_DIR)

# Switching the Current Python Directory
chd = os.chdir('/private/var/mobile/Containers/Data/Application/DAEB6B2A-D9F8-4574-A2B5-A0EA119B72AE/Documents')
CURR_DIR2 = os.getcwd()
print('Current Directory (after change): ', CURR_DIR2)

# List out all files and sub-folders within current working direcotry
os.listdir()

# Make a new folder within the current project directory
os.mkdir('foldername1')

# Rename any named file or folder within the currenty directory
os.rename('foldername1', 'foldername2now')

# Remove empty folder within the current working path
os.rmdir('foldername2now')

# Delete a file from the directory
try:
    os.remove('filenametobedeleted')
except:
    print('either does not exist or already deleted.')

# Remcursive delete a directory within the cwd
try:
    shutil.rmtree('folderwithcontents')
except:
    print('either does not exist or already deleted.')
    
   
    
     
# Timer Function

def timer(startTime, endTime):
    '''
    import time
    start = time.time()
    <block(s) of code>
    end = time.time()
    '''
    seconds = 0
    seconds = endTime-startTime
    minutes = int(seconds//60)
    remainder = int(seconds%60)
    print('Process took:', minutes, ' min ', remainder, ' seconds to perform.\n')

# Common Imports

import pandas as pd
import numpy as np
from ftplib import FTP
import warnings
import time
import datetime as dt
import datetime
from datetime import timedelta

# Jupyter Notebook Display Settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
      
       
         
# Example - Creating a multiIndexed DataFrame

midx = pd.MultiIndex(levels=[['lama', 'cow', 'falcon'], 
                             ['speed', 'weight', 'length']],
                      codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2],
                             [0, 1, 2, 0, 1, 2, 0, 1, 2]])

df = pd.DataFrame(index=midx, columns=['big', 'small'],
                   data=[[45, 30], [200, 100], [1.5, 1], [30, 20],
                         [250, 150], [1.5, 0.8], [320, 250],
                         [1, 0.8], [0.3, 0.2]])
df = df.T
df2 = df.copy()

# Flatten Hierarchical Index Columns (2d -> 1d) for MultiIndexed DataFrames

mi = df2.columns
ind = pd.Index([e[0] + e[1] for e in mi.tolist()])
df2.columns = ind


print(df)
print(df2)

# Create Backbone DataFrame with all date indexes

def make_date_column(date1, date2):
    ''' 
    returns a dataFrame with a column of all dates between date1 and date2
    date1 = stat date,
    date2 = end date
    '''
    df = pd.DataFrame({'Date':pd.date_range(date1, date2).to_list()})
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['Week'] = df['Date'].dt.week
    return df

tempdf = make_date_column('2020-01-01', '2020-12-31')
print(tempdf)

# Dict <--> DataFrame Week Indexing

def make_weekdict(numberOfWeeks):
    '''
    Starting Date for Week #1:  2019-12-1,
    Ending Date for Week #1:    2019-12-8,
    Starting Date for Week #2:  2019-12-8,
    Ending Date for Week #2:    2019-12-15
    ...
    '''
    date1 = datetime.date(2019,12,29)
    week = timedelta(days=7)
    weekdict = {1:[date1, date1+week]}
    x=2
    while x < numberOfWeeks:
        weekdict[x] = [weekdict[x-1][1], weekdict[x-1][1]+week]
        x += 1
    for key,value in weekdict.items():
        weekdict[key] = ['{:%Y-%m-%d}'.format(x) for x in value]
    return weekdict


def make_weekdict_input(numberOfWeeks, startyear, startmonth, startday):
    '''
    Starting Date for Week #1:  2019-12-1,
    Ending Date for Week #1:    2019-12-8,
    Starting Date for Week #2:  2019-12-8,
    Ending Date for Week #2:    2019-12-15
    ...
    '''
    date1 = datetime.date(startyear,startmonth,startday)
    week = timedelta(days=7)
    weekdict = {1:[date1, date1+week]}
    x=2
    while x < numberOfWeeks:
        weekdict[x] = [weekdict[x-1][1], weekdict[x-1][1]+week]
        x += 1
    for key,value in weekdict.items():
        weekdict[key] = ['{:%Y-%m-%d}'.format(x) for x in value]

    return weekdict

def show_week_bounds(weekdict):
    weekdictt = weekdict.copy()
    keylist = list(weekdictt.keys())
    weeklist = list(weekdictt.values())
    x=0
    while x < len(keylist):
        print(keylist[x], '<--', weeklist[x], '\n')
        x +=1
    return

def return_week_index(date):
    weekdict = make_weekdict(50)
    indexlist = list(weekdict.keys())
    weeklist = list(weekdict.values())
    x=0
    while x < len(indexlist):
        if (weeklist[x][0] <= date) & (date < weeklist[x][1]):
            return indexlist[x]
        x += 1

def return_week_start(date):
    # if want week end, change 0 in return to 1
    weekdict = make_weekdict(50)
    indexlist = list(weekdict.keys())
    weeklist = list(weekdict.values())
    x=0
    while x < len(indexlist):
        if (weeklist[x][0] <= date) & (date < weeklist[x][1]):
            return weeklist[x][0]
        x += 1

# Example Application    
df5['Week Index'] = df5['Postdate'].apply(lambda x: return_week_index(x))
df5['Week Start'] = df5['Postdate'].apply(lambda x: return_week_start(x))
weekdf = df5[['Week Index', 'Week Start']].drop_duplicates(keep='first').rename(columns={'Week Index':'Week'})
