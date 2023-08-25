"""
Data that we have

    Champions:
        Games played
        Pick ban
        Number of  unique players
        WR
        KDA
        CS/min
        Gold/min
        DPS
        KP
        Kill share
        Gold share
        Role

    Player stats:
        Games played
        Pick ban
        WR
        KDA
        CS/min
        Gold/min
        DPS
        KP
        Kill share
        Gold share
        Role
        Champions Played

    Team stats:
        Standing
        Streak
        WR
        Previous scores against same team
"""
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

# CSV_NAME1 = "LoL Project Data Spreadsheet - Sheet1.csv"
CSV_NAME2 = "LoL Project Data Spreadsheet - lckSumSznChamps.csv"
CSV_NAME3 = ""
CSV_NAME4 = ""

def main():
    readCSV(CSV_NAME2)

def readCSV(csv):
    dict = {}
    champList = []
    
    champStatsList=[]
    df = pd.read_csv(csv)
    for i in range(len(df.index)):
        champList.append(df['Champion'][i])
    
    for index, row in df.iterrows():
        champStats = []
        for column in df.columns:
            entry = row[column]
            champStats.append(entry)
        champStatsList.append(champStats)
    
    for i in range(len(champList)):
        dict.update({champList[i]:champStatsList[i]})

def findSynergies(champ, csv):
    df = pd.read_csv(csv)
    pass
        
main()










# def urlList():
#     url = ""

# def scrape(url):
#     website = requests.get(url)
#     soup1 = BeautifulSoup(website.text, 'lxml')
#     soup2 = BeautifulSoup(soup1.prettify(), 'lxml')
#     print(soup2)

#     # champList = soup2.find_all('span', {'class': 'markup-object-name'})
#     # for champ in champList:
#     #     print(champ.get_text())

# scrape("https://lol.fandom.com/wiki/LCK/2023_Season/Spring_Season/Champion_Statistics")