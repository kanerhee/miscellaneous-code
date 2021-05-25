def timer(starttime, endtime):
    # import time
    # startTime = time.time()
    # <block(s) of code>
    # endTime = time.time()
    seconds = 0
    seconds = endtime-starttime
    minutes = int(seconds//60)
    remainder = int(seconds%60)
    print('Process took:', minutes, ' min ', remainder, ' seconds to perform.\n')
    
def printlength(df):
    print('length: ', len(df), ' rows. \n')
    return

##########################################################################################

def computeDRA(x, dfmain):
    # input X is a company
    dft = dfmain.copy()
    dft = dft[dft['company'] == x]
    output = list(dft['Daily Raw Attempts'])
    return output

def computeAVG(x, dfmain):
    # input X is a company
    dft = dfmain.copy()
    dft = dft[dft['company'] == x]
    output = np.array(list(dft['Daily Raw Attempts'])).mean()
    return output

def computeSTD(x, dfmain):
    # input X is a company
    dft = dfmain.copy()
    dft = dft[dft['company'] == x]
    output = np.array(list(dft['Daily Raw Attempts'])).std(ddof=1)
    return output

def computeLAST(x, dfmain):
    # input X is a company
    dft = dfmain.copy()
    dft = dft[dft['company'] == x]
    output = list(dft['Daily Raw Attempts'])[-1]
    return output

##########################################################################################

def append_usage_alerts_to_master(dfmain2):
    
    df_old = pd.read_csv('usage_alerts_results_master.csv')
    
    if 'Unnamed: 0' in df_old:
        df_old.drop(columns=['Unnamed: 0'], inplace=True)
    
    colNames = df_old.columns
    
    dfmain3 = dfmain2.copy()[['company', 'start', 'stop', 'current', 'daily_raw_attempts',
                            'Total Raw Attempts', 'Average', 'Standard Deviation',
                           'threshold (= avg - 2*std)', 'last', 'TEST']]
    
    df_new = pd.DataFrame(data=dfmain3, columns=colNames)
    
    if 'Unnamed: 0' in df_new:
        df_new.drop(columns=['Unnamed: 0'], inplace=True)
        
    df_new['start'] = pd.to_datetime(df_new['start']).dt.normalize()
    df_new['stop'] = pd.to_datetime(df_new['stop']).dt.normalize()
    df_new['current'] = pd.to_datetime(df_new['current']).dt.normalize()    

    df_complete = pd.concat([df_old, df_new], axis=0)
    
    df_complete['start'] = pd.to_datetime(df_complete['start']).dt.normalize()
    df_complete['stop'] = pd.to_datetime(df_complete['stop']).dt.normalize()
    df_complete['current'] = pd.to_datetime(df_complete['current']).dt.normalize()   
    
    df_complete = df_complete.drop_duplicates(subset=['start', 'stop', 'current', 'company'], keep='first')
    
    df_complete.to_csv('usage_alerts_results_master.csv', index=False)
    
    return df_complete

##########################################################################################

def calculate_usage_alerts(df):

    datestring = datetime.today().strftime('%Y_%m_%d_')

    filenam = datestring + 'usage_alerts_results.csv'
    print('filename: ', filenam)

    # i. FOR DAILY RAW ATTEMPTS

    # Create top 100 df, and take list of top 10 companies
    df2 = df.copy()
    df2 = df2.groupby(['company']).agg({'Daily Raw Attempts':'sum'})
    df2 = df2.sort_values(by='Daily Raw Attempts', ascending=False)
    df2 = df2.reset_index().reset_index()

    df100 = df2[df2['index'] < 105]
    top_companies = list(df100['company'])

    print('Length of raw dataset: ', len(df), ' rows.')

    # make dfmain (df of just the top 100 countries)

    dfmain = df[df['company'].isin(top_companies)]
    print('Length after subsetting top 100 companies: ', len(dfmain), ' rows.')

    # get today's date, calculate dates for presvious N-day lookback window

    todaysdate = datetime.today() #.strftime('%Y-%m-%d-%H:%M:%S')

    delta1 = timedelta(days = 1)
    delta30 = timedelta(days = 30)

    upperbound = todaysdate - delta1
    lowerbound  = upperbound - delta30

    print('Todays Date: ', todaysdate)
    print('Yesterdays Date: ', upperbound)
    print('Start of 30 day previous: ', lowerbound)

    # subset dfmain to the previous N-day lookback window
    dfmain['activity_date'] = pd.to_datetime(dfmain['activity_date']).dt.normalize()
    dfmain = dfmain[(dfmain['activity_date'] >= lowerbound) & (dfmain['activity_date'] <= upperbound)]
    print('Length after subsetting dates: ', len(dfmain), ' rows.')

    dfmain2 = dfmain.copy()

    dfmain2 = dfmain2.groupby(['company']).agg({'Daily Raw Attempts':'sum'})
    dfmain2 = dfmain2.reset_index()

    dfmain2['start'] = lowerbound
    dfmain2['start'] = pd.to_datetime(dfmain2['start']).dt.normalize()
    dfmain2['stop'] = upperbound
    dfmain2['stop'] = pd.to_datetime(dfmain2['stop']).dt.normalize()
    dfmain2['current'] = todaysdate
    dfmain2['current'] = pd.to_datetime(dfmain2['current']).dt.normalize()

    dfmain2.rename(columns={'Daily Raw Attempts':'Total Raw Attempts'}, inplace=True)

    dfmain2['daily_raw_attempts'] = dfmain2['company'].apply(lambda x: computeDRA(x, dfmain))
    dfmain2['Average'] = dfmain2['company'].apply(lambda x: computeAVG(x, dfmain))
    dfmain2['Standard Deviation'] = dfmain2['company'].apply(lambda x: computeSTD(x, dfmain))
    dfmain2['last'] = dfmain2['company'].apply(lambda x: computeLAST(x, dfmain))

    dfmain2['threshold (= avg - 2*std)'] = dfmain2['Average'] - (2*dfmain2['Standard Deviation'])
    dfmain2['TEST'] = (dfmain2['last'] < dfmain2['threshold (= avg - 2*std)'])

    dfmain2 = dfmain2[['company', 'start', 'stop', 'current', 'daily_raw_attempts', 'Total Raw Attempts', 
                       'Average', 'Standard Deviation', 'threshold (= avg - 2*std)', 'last', 'TEST']]

    dfmain2.to_csv(filenam)
    ndf = append_usage_alerts_to_master(dfmain2)

    print('\n', dfmain2.TEST.value_counts(), '\n')

    return dfmain2, ndf

def calculate_did_loss_alerts(hf):

    # max_did_count - # of DIDs that they came up with time of signup
    # current_did_count - Current # of dids
    # Formula:   | max_did_count - current_did_count | >= 1

    dfd = hf.copy()

    dfd = dfd.sort_values(by='max_did_count', ascending=False)

    dfd['did_delta'] = dfd['max_did_count'] - dfd['current_did_count']

    dfd = dfd[['parent_company', 'parent_customerkey', 'did_delta', 'max_did_date', 'max_did_count', 'current_did_date', 'current_did_count', 'last_processed_date',
              'last_inbound_usage_ts', 'last_outbound_usage_ts', 'resellerid']]

    dfd.rename(columns={
        'parent_company':'company',
        'parent_customerkey':'companyCK',
        'last_inbound_usage_ts':'lastIBusageTS',
        'last_outbound_usage_ts':'lastOBusageTS'
    }, inplace=True)

    dfd = dfd.sort_values(by='did_delta', ascending=False)

    dfd2 = dfd.copy()

    dfd2 = dfd2[dfd2['did_delta'] > 0]
    print('dfd2: ', printlength(dfd2))

    filenam2 = datestring + 'did_loss_alerts_results.csv'
    print('filename: ', filenam2)
    dfd2.to_csv(filenam2)

    dfd_old = pd.read_csv('did_loss_alerts_master.csv')
    if 'Unnamed: 0' in dfd_old:
        dfd_old.drop(columns=['Unnamed: 0'], inplace=True)
    colNames = dfd_old.columns
    dfd_new = pd.DataFrame(data=dfd2, columns=colNames)
    df_complete = pd.concat([dfd_old, dfd_new], axis=0)
    df_complete = df_complete.drop_duplicates(subset=['max_did_date', 'current_did_date', 'did_delta', 'company'], keep='first')
    df_complete.to_csv('did_loss_alerts_master.csv', index=False)

    return dfd2, df_complete

##########################################################################################

import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta
import time
from ftplib import FTP
import domo_python
import warnings

start3 = time.time()

warnings.filterwarnings('ignore')

client_id = '35d820ac-0e16-437c-92e9-a9068f0b3116'
client_secret = '767614aca6de967a35fec9cbe41bb801acfe7fa73f26524f1e480c13110f8259'
    
datasetdict = {
             'fax_daily_comined_2020_etl_output_condensed' : 'fa2c63a3-a39c-4dff-b621-c9c62be1a2e7',
             'bi.usage_combined_daily'            : 'eeff7605-9daa-43c7-98de-a3d483a67252',
             'bi.high_premium_usage'              : '08bb5025-139e-484d-913b-f8bb4132a08f',
             'bi.did_corp_count'                  : '4996f1d3-c7e7-4005-9646-5ed2741d2fb2',
             'evoice_onebox_daily_transactions'   : 'f70196d7-8e41-4304-a9b1-97934f83b353',
             'dfr_act_0010'                       : 'dc66c248-5861-46ce-b4d4-bbd1509e66d6',
             'dfr_act_0010_2020_only'             : '888f5666-02ac-4783-9c11-511dce432e4a',
             'fin_0010'                           : 'e14c2e18-e514-4a0a-adc9-fddd2a79cc89'
}

start = time.time()

df = domo_python.domo_csv_to_dataframe(datasetdict['fax_daily_comined_2020_etl_output_condensed'], client_id, client_secret)

print('Finished pulling df - fax_daily_comined_2020_etl_output_condensed')

printlength(df)

end = time.time()

timer(start, end)

start2 = time.time()

hf = domo_python.domo_csv_to_dataframe(datasetdict['bi.did_corp_count'], client_id, client_secret)

if '_BATCH_ID_' in hf:
    hf.drop(columns=['_BATCH_ID_', '_BATCH_LAST_RUN_'], inplace=True)

print('Finished pulling hf - bi.did_corp_count')

printlength(hf)

end2 = time.time()

timer(start2, end2)

# i. usage alerts
df_today, df_complete = calculate_usage_alerts(df)

# ii. did loss alerts
dfdid_today, dfdid_complete = calculate_did_loss_alerts(hf)

end3 = time.time()

print('Whole ', timer(start3, end3))