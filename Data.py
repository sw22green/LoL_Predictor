from bs4 import BeautifulSoup
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CSV_NAME2 = "LoL Project Data Spreadsheet - lckSumSznChamps.csv"
CSV_NAME3 = ""
CSV_NAME4 = ""

def main():
    allData("https://lol.fandom.com/wiki/LCK/2023_Season/Spring_Season/Match_History")

def allData(url):
    options = Options()
    options.add_argument("--headless=new")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--disk-cache-dir=/path/to/cache')
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    html = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(html, 'lxml')

    # Format: [Blue, Red, Winner, Blue, Red, Winner, Blue ...]
    teamsList = scrapeTeams(soup) 

    # Format: [Blue1, Blue2, Blue3, Blue4,Blue5, Red1, Red2, Red3, Red4, Red5, Blue1 ...]
    playerList = scrapeRosters(soup)
    
    # Format: [Blue1, Blue2, Blue3, Blue4,Blue5, Red1, Red2, Red3, Red4, Red5, Blue1 ...]
    picksList = scrapePicks(soup)

    # Blue or Red
    winSideList = winnerSide(teamsList)
    print(teamsList)

def scrapeTeams(soup):
    teamNameData = soup.find(class_ = "table-wide").find_all('img', alt = True)
    teamsList = []
    for team in teamNameData:
        teamsList.append((team['alt'])[:-8])

    return teamsList


def scrapeRosters(soup):
    playerNameData = soup.find_all(class_ = "catlink-players pWAG pWAN to_hasTooltip")
    playerList = []
    for player in playerNameData:
        playerList.append(player['data-to-id'])

    return playerList

def scrapePicks(soup):
    count = 0
    champPickedData = soup.find_all(class_ = "multirow-highlighter")
    picksList = []
    for champHTML in champPickedData:
        for champPicked in champHTML.find_all(class_ = "sprite champion-sprite"):
            if(count%20 > 9): picksList.append(champPicked['title'])
            count+=1

    return picksList


def winnerSide(teamsList):
    winSideList = []
    for i in range(len(teamsList)//3-1):
        if(teamsList[3*(i+1)-1]==(teamsList[3*(i+1)-2])): winSideList.append("Red")
        else: winSideList.append("Blue")
    
    return winSideList

main()
# def readCSV(csv):
#     dict = {}
#     champList = []
    
#     champStatsList=[]
#     df = pd.read_csv(csv)
#     for i in range(len(df.index)):
#         champList.append(df['Champion'][i])
    
#     for index, row in df.iterrows():
#         champStats = []
#         for column in df.columns:
#             entry = row[column]
#             champStats.append(entry)
#         champStatsList.append(champStats)
    
#     for i in range(len(champList)):
#         dict.update({champList[i]:champStatsList[i]})

# def findSynergies(champ, csv):
#     df = pd.read_csv(csv)
#     pass
        
# main()




