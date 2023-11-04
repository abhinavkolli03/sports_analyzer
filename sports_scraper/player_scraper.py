from selenium import webdriver
import time
import pandas as pd
driver = webdriver.Chrome()

website = "https://www.nba.com/stats/players/bio?Season=2000-01&SeasonType=Regular%20Season"




# website = 'https://ww.adamchoi.cok.uk/overs.detailed'
# path = '/Users/abhin/OneDrive/Desktop/chrome-win32'
# driver.get(website)

# # from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options
# # from webdriver_manager.chrome import ChromeDriverManager
# # import time
# # import pandas as pd

# # from bs4 import BeautifulSoup
# # from urllib.request import Request, urlopen
# # import re

# # chrome_options = Options()
# # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


# # def retrieve_season_stats(URL):
# #     driver = webdriver.Chrome(ChromeDriverManager().install())
    
# #     driver.get(URL)
# #     time.sleep(3)

# #     driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
# #     time.sleep(3)
    
# #     driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select').click()
# #     time.sleep(3)
    
# #     player_bio = (driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[2]/table/tbody').text)
# #     player_list = driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]').text.split('\n')

# #     driver.quit()
    
# #     headers = ['PLAYER', 'TEAM', 'AGE', 'HEIGHT', 'WEIGHT', 'COLLEGE COUNTRY',
# #                     'DRAFT YEAR', 'DRAFT ROUND', 'DRAFT NUMBER','GP', 'PTS', 'REB',
# #                     'AST', 'NETRTG', 'OREB%', 'DREB%', 'USG%', 'TS%', 'AST%']    
    
# #     table_rows = [x for x in player_list if len(x.split(' ')) > 15][1:]
    
# def BRING_SEASONAL_PLAYER_STATS(URL_LINK):
#     driver.get(URL_LINK)
#     time.sleep(3)
    
#     driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
#     time.sleep(3)

#     driver.find_element_by_xpath(
#         '/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select'
#     ).click()
#     time.sleep(3)
    
#     driver.find_element_by_xpath(
#         '/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select/option[1]'
#     ).click()
#     time.sleep(3)

#     PLAYER_LIST = (driver.find_element_by_xpath(
#         '/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[2]/table/tbody'
#     ).text)


#     LIST_OF_PLAYERS = driver.find_element_by_xpath(
#         '/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]'
#     ).text.split('\n')

#     driver.quit()
    
#     TABLE_ROWS = [x for x in LIST_OF_PLAYERS if len(x.split(' ')) > 15][1:]
#     TABLE_HEADERS = [
#                      'PLAYER',
#                      'TEAM',
#                      'AGE',
#                      'HEIGHT',
#                      'WEIGHT',
#                      'COLLEGE COUNTRY',
#                      'DRAFT YEAR',
#                      'DRAFT ROUND',
#                      'DRAFT NUMBER',
#                      'GP',
#                      'PTS',
#                      'REB',
#                      'AST',
#                      'NETRTG',
#                      'OREB%',
#                      'DREB%',
#                      'USG%',
#                      'TS%',
#                      'AST%']
    
#     REVERSED_STRINGS_FOR_LAST_13_COLUMNS = [x[::-1].split(' ')[:13] for x in TABLE_ROWS]
#     STRINGS_FOR_LAST_13_COLUMNS = [[x[::-1] for x in i] for i in REVERSED_STRINGS_FOR_LAST_13_COLUMNS]    
    
#     df_1st_Column = pd.DataFrame(PLAYER_LIST.split('\n'), columns=['PLAYER'])
#     df_2nd_to_5th_Columns = pd.DataFrame([x.split(' ')[:4] for x in TABLE_ROWS], 
#                                  columns=['TEAM', 'AGE', 'HEIGHT', 'WEIGHT'])
#     df_6th_and_7th_Columns = pd.DataFrame([' '.join([x[::-1] for x in i][::-1]) for i in 
#         [' '.join(x.split(' ')[4:])[::-1].split(' ')[13:] for x in TABLE_ROWS]
#     ], columns=['COLLEGE COUNTRY'])
#     df_Last_13_Columns = pd.DataFrame(STRINGS_FOR_LAST_13_COLUMNS)[list(reversed([i for i in range(13)]))]
#     df_Last_13_Columns.columns = TABLE_HEADERS[-13:]
    
#     df_Players = pd.concat([df_1st_Column, 
#                             df_2nd_to_5th_Columns, 
#                             df_6th_and_7th_Columns, 
#                             df_Last_13_Columns
#                            ], axis=1)
    
#     return df_Players


# PAGE_URL = 'https://www.nba.com/stats/players/bio/?Season=2000-01&SeasonType=Regular%20Season'
# df_Players = BRING_SEASONAL_PLAYER_STATS(PAGE_URL)