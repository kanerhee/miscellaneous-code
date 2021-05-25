import pandas as pd
import numpy as np
import time
import datetime
import html5lib
import requests
from bs4 import BeautifulSoup, SoupStrainer
import httplib2

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


def column_cleaner(m):

    newcoldict = {
    'Def Interceptions_Int':'DEF_INT',
    'Def Interceptions_PD' :'DEF_PD',
    'Def Interceptions_TD' :'DEF_TD',
    'Def Interceptions_Yds':'DEF_INT_YDS',
    'Def. Snaps_Num'       :'DEF_NUM_SNAPS',
    'Def. Snaps_Pct'       :'DEF_PCT_SNAPS',
    'Fumbles_FF'           :'DEF_FF_FF',
    'Fumbles_FL'           :'DEF_FF_FL',
    'Fumbles_FR'           :'DEF_FF_FR',
    'Fumbles_Fmb'          :'DEF_FF_FMB',
    'Fumbles_TD'           :'DEF_FF_TD',
    'Fumbles_Yds'          :'DEF_FF_YDS',
    'Namex_Namey'          :'NAME',
    'Off. Snaps_Num'       :'OFF_NUM_SNAPS',
    'Off. Snaps_Pct'       :'OFF_PCT_SNAPS',
    'Passing_AY/A'         :'OFF_PASS_AVG_YPATT',
    'Passing_Att'          :'OFF_PASS_ATT',
    'Passing_Cmp'          :'OFF_PASS_CMP',
    'Passing_Cmp%'         :'OFF_PASS_CMP_PCT',
    'Passing_Int'          :'OFF_INT',
    'Passing_Rate'         :'OFF_PASS_RATING',
    'Passing_Sk'           :'OFF_SCKS',
    'Passing_TD'           :'OFF_PASS_TD',
    'Passing_Y/A'          :'OFF_PASS_YPATT',
    'Passing_Yds'          :'OFF_PASS_YDS',
    'Passing_Yds.1'        :'OFF_PASS_YDS_1',
    'Posx_Posy'            :'POSITION',
    'Punting_Blck'         :'PUNT_BLOCK',
    'Punting_Pnt'          :'PUNT_PUNT',
    'Punting_Y/P'          :'PUNT_YPP',
    'Punting_Yds'          :'PUNT_REC_YDS',
    'Receiving_Ctch%'      :'OFF_REC_PCT',
    'Receiving_Rec'        :'OFF_REC_REC',
    'Receiving_TD'         :'OFF_REC_TD',
    'Receiving_Tgt'        :'OFF_REC_TGT',
    'Receiving_Y/R'        :'OFF_REC_YPREC',
    'Receiving_Y/Tgt'      :'OFF_REC_YPTGT',
    'Receiving_Yds'        :'OFF_REC_YDS',
    'Rushing_Att'          :'OFF_RUSH_ATT',
    'Rushing_TD'           :'OFF_RUSH_TD',
    'Rushing_Y/A'          :'OFF_RUSH_YPATT',
    'Rushing_Yds'          :'OFF_RUSH_YDS',
    'ST Snaps_Num'         :'ST_NUM_SNAPS',
    'ST Snaps_Pct'         :'ST_PCT_SNAPS',
    'Scoring_FG%'          :'SCOR_FGP',
    'Scoring_FGA'          :'SCOR_FGA',
    'Scoring_FGM'          :'SCOR_PTM',
    'Scoring_Pts'          :'SCOR_PTS',
    'Scoring_TD'           :'SCOR_TD',
    'Scoring_XP%'          :'SCOR_XPP',
    'Scoring_XPA'          :'SCOR_XPA',
    'Scoring_XPM'          :'SCOR_XPM',
    'Tackles_Ast'          :'DEF_TCKL_AST',
    'Tackles_Comb'         :'DEF_TCKL_CMB',
    'Tackles_QBHits'       :'DEF_TCKL_QBHT',
    'Tackles_Solo'         :'DEF_TCKL_SOLO',
    'Tackles_TFL'          :'DEF_TCKL_TFL',
    'Teamx_Teamy'          :'TEAM',
    'Unnamed: 0_level_0_Rk'                :'GAMEPLAYED',
    'Unnamed: 10_level_0_Sk'               :'b',
    'Unnamed: 16_level_0_Sk'               :'c',
    'Unnamed: 1_level_0_Date'              :'DATE',
    'Unnamed: 2_level_0_G#'                :'GAMENUM',
    'Unnamed: 3_level_0_Week'              :'WEEKNUM',
    'Unnamed: 4_level_0_Age'               :'AGE',
    'Unnamed: 5_level_0_Tm'                :'TM',
    'Unnamed: 6_level_0_Unnamed: 6_level_1':'HOMEAWAY',
    'Unnamed: 7_level_0_Opp'               :'AGAINST',
    'Unnamed: 8_level_0_Result'            :'SCORE',
    'Unnamed: 9_level_0_GS'                :'START'
    }

    if (             'Namex',              'Namey') in m:
        mi = m.columns
        ind = list(str(e[0]+'_'+e[1]) for e in mi.tolist())
        m.columns = ind

    if list(m.columns) == ind:
        m.rename(columns=newcoldict, inplace=True)

    m = m[['TEAM', 'NAME', 'POSITION',

           'GAMEPLAYED', 'b', 'c', 'DATE', 'GAMENUM', 'WEEKNUM', 'AGE', 'TM', 'HOMEAWAY', 'AGAINST', 'SCORE', 'START',

           'OFF_NUM_SNAPS', 'OFF_PCT_SNAPS',

           'OFF_PASS_AVG_YPATT', 'OFF_PASS_ATT', 'OFF_PASS_CMP',
           'OFF_PASS_CMP_PCT', 'OFF_INT', 'OFF_PASS_RATING', 'OFF_SCKS',
           'OFF_PASS_TD', 'OFF_PASS_YPATT', 'OFF_PASS_YDS', 'OFF_PASS_YDS_1',

           'OFF_REC_PCT', 'OFF_REC_REC', 'OFF_REC_TD', 'OFF_REC_TGT',
           'OFF_REC_YPREC', 'OFF_REC_YPTGT', 'OFF_REC_YDS',

           'OFF_RUSH_ATT', 'OFF_RUSH_TD', 'OFF_RUSH_YPATT', 'OFF_RUSH_YDS',

           'DEF_NUM_SNAPS', 'DEF_PCT_SNAPS',
           'DEF_TCKL_AST', 'DEF_TCKL_CMB', 'DEF_TCKL_QBHT', 'DEF_TCKL_SOLO', 'DEF_TCKL_TFL',
           'DEF_INT', 'DEF_INT_YDS', 'DEF_PD', 'DEF_TD',
           'DEF_FF_FF', 'DEF_FF_FL', 'DEF_FF_FR', 'DEF_FF_FMB','DEF_FF_TD', 'DEF_FF_YDS',

           'ST_NUM_SNAPS', 'ST_PCT_SNAPS',
           'SCOR_FGP', 'SCOR_FGA', 'SCOR_PTM', 'SCOR_PTS',
           'SCOR_TD', 'SCOR_XPP', 'SCOR_XPA', 'SCOR_XPM',
           'PUNT_BLOCK', 'PUNT_PUNT', 'PUNT_YPP', 'PUNT_REC_YDS',
          ]]

    return m


def make_udf(teamrosterdict):
    dfl = []
    for key,value in teamrosterdict.items():
        http = httplib2.Http()
        status, response = http.request(teamrosterdict[key])
    #     print(status, '\n\n\n\n')

        for link in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a')):

            if link.has_attr('href'):
                if ('.htm' in str(link)) & ('title=' not in str(link)) & ('/officials/' not in str(link)):
                    if ('/about/' not in str(link)) & ('/coaches/' not in str(link)) & ('/draft' not in str(link)):
                        if ('/players/' in str(link)) & ('.htm' in str(link)):
    #                     if ('/rai/2019_' not in str(link)) & ('2019' not in str(link)):
                            data = (key, link.text, str(link))
                            dfl.append(data)
    #                         print(data)

    stem = 'https://www.pro-football-reference.com'
    udf = pd.DataFrame(dfl, columns=['team', 'name', 'url2'])
    udf['url'] = stem+udf['url2'].apply(lambda x: x[9:32])
    udf = udf[['team', 'name', 'url']]
    print('\n')
    return udf


def make_udf_positions(udf):
    poslist = []
    udf['Position'] = 'n/a'
    x=0
    print('Progress: ')
    while x < len(udf):

        try:

            url = udf.url[x]
            get_url = requests.get(url)
            get_text = get_url.text

            soup = BeautifulSoup(get_text, 'html.parser')

            bname = list(soup.find_all('p'))
            poname = bname[1].text[1:16]
            poname = poname.replace('Position: ','')
            poname = poname.replace('\n', '')
            poname = poname.replace('\t', '')
            if x % 10 == 0:
                print('x: ', x, ' - ', poname)
            poslist.append(poname)

        except:

            print(x, 'failed')

        x += 1

    udf['Position'] = poslist
    udf['url2'] = udf['url'].str.replace('.htm', '/gamelog/2019/')

    udf = udf[['team', 'name', 'Position', 'url', 'url2']]
    print('Done with make_udf_positions \n')
    return udf


def make_m(udf):

    wklist = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0,
              8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0,
              15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0]

    dflist = []

    y=0
    while y < len(udf):

        try:
            url = udf.url2[y]
            df = pd.read_html(url)[0]
            df = df[df[('Unnamed: 3_level_0', 'Week')].isin(wklist)]
            df[('Namex', 'Namey')] = udf.name[y]
            df[('Teamx', 'Teamy')] = udf.team[y]
            df[('Posx', 'Posy')] = udf.Position[y]
            if y % 10 == 0:
                print('at Y = ', y)
        except:
            print('y : ', y, 'failed.')

        dflist.append(df)
        y += 1

    m = pd.concat(dflist)
    print('Done with make_m\n')
    return m


teamrosterdict = {
    # AFC
    'rai':'https://www.pro-football-reference.com/teams/rai/2019_roster.htm',
    'den':'https://www.pro-football-reference.com/teams/den/2019_roster.htm',
    'sdg':'https://www.pro-football-reference.com/teams/sdg/2019_roster.htm',
    'kan':'https://www.pro-football-reference.com/teams/kan/2019_roster.htm',

    'clt':'https://www.pro-football-reference.com/teams/clt/2019_roster.htm',
    'htx':'https://www.pro-football-reference.com/teams/htx/2019_roster.htm',
    'oti':'https://www.pro-football-reference.com/teams/oti/2019_roster.htm',
    'jax':'https://www.pro-football-reference.com/teams/jax/2019_roster.htm',

    'cin':'https://www.pro-football-reference.com/teams/cin/2019_roster.htm',
    'pit':'https://www.pro-football-reference.com/teams/pit/2019_roster.htm',
    'cle':'https://www.pro-football-reference.com/teams/cle/2019_roster.htm',
    'rav':'https://www.pro-football-reference.com/teams/rav/2019_roster.htm',

    'nwe':'https://www.pro-football-reference.com/teams/nwe/2019_roster.htm',
    'nyj':'https://www.pro-football-reference.com/teams/nyj/2019_roster.htm',
    'buf':'https://www.pro-football-reference.com/teams/buf/2019_roster.htm',
    'mia':'https://www.pro-football-reference.com/teams/mia/2019_roster.htm',

    # NFC
    'ram':'https://www.pro-football-reference.com/teams/ram/2019_roster.htm',
    'sfo':'https://www.pro-football-reference.com/teams/sfo/2019_roster.htm',
    'crd':'https://www.pro-football-reference.com/teams/crd/2019_roster.htm',
    'sea':'https://www.pro-football-reference.com/teams/sea/2019_roster.htm',

    'car':'https://www.pro-football-reference.com/teams/car/2019_roster.htm',
    'tam':'https://www.pro-football-reference.com/teams/tam/2019_roster.htm',
    'nor':'https://www.pro-football-reference.com/teams/nor/2019_roster.htm',
    'atl':'https://www.pro-football-reference.com/teams/atl/2019_roster.htm',

    'min':'https://www.pro-football-reference.com/teams/min/2019_roster.htm',
    'det':'https://www.pro-football-reference.com/teams/det/2019_roster.htm',
    'chi':'https://www.pro-football-reference.com/teams/chi/2019_roster.htm',
    'gnb':'https://www.pro-football-reference.com/teams/gnb/2019_roster.htm',

    'phi':'https://www.pro-football-reference.com/teams/phi/2019_roster.htm',
    'nyg':'https://www.pro-football-reference.com/teams/nyg/2019_roster.htm',
    'was':'https://www.pro-football-reference.com/teams/was/2019_roster.htm',
    'dal':'https://www.pro-football-reference.com/teams/dal/2019_roster.htm'
}



udf = make_udf_positions(make_udf(teamrosterdict))
m = column_cleaner(make_m(udf))

m
