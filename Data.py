from bs4 import BeautifulSoup
import csv
import pandas as pd
from itertools import chain
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CSV_NAME2 = "LoL Project Data Spreadsheet - lckSumSznChamps.csv"
CSV_NAME3 = ""
CSV_NAME4 = ""

def main():
    # # Spring Season
    # allData("https://lol.fandom.com/wiki/LCK/2023_Season/Spring_Season/Match_History")
    # # Spring Playoff
    # allData("https://lol.fandom.com/wiki/LCK/2023_Season/Spring_Playoffs/Match_History")
    # # Summer Season
    # allData("https://lol.fandom.com/wiki/LCK/2023_Season/Summer_Season/Match_History")
    # # Summer Playoff
    # allData("https://lol.fandom.com/wiki/LCK/2023_Season/Summer_Season/Match_History")


    urlList = ["https://lol.fandom.com/wiki/LCK/2023_Season/Spring_Season/Match_History", 
               "https://lol.fandom.com/wiki/LCK/2023_Season/Spring_Playoffs/Match_History", 
               "https://lol.fandom.com/wiki/LCK/2023_Season/Summer_Season/Match_History", 
               "https://lol.fandom.com/wiki/LCK/2023_Season/Summer_Playoffs/Match_History"]
    
    allTeams = []
    allPlayers = []
    allPicks = []
    allWinSide = []
    
    for url in urlList:
        info = allData(url)
        allTeams.append(info[0])
        allPlayers.append(info[1])
        allPicks.append(info[2])
        allWinSide.append(info[3])
        print("ANDYYYYYY BIG")

    allTeams = list(chain.from_iterable(allTeams))
    allPlayers = list(chain.from_iterable(allPlayers))
    allPicks = list(chain.from_iterable(allPicks))
    allWinSide = list(chain.from_iterable(allWinSide))


    blueTeam = []
    redTeam = []
    winnerTeam = []
    
    bluePlayerTop = []
    bluePlayerJug = []
    bluePlayerMid = []
    bluePlayerBot = []
    bluePlayerSup = []

    redPlayerTop = []
    redPlayerJug = []
    redPlayerMid = []
    redPlayerBot = []
    redPlayerSup = []

    blueChampTop= []
    blueChampJug = []
    blueChampMid = []
    blueChampBot = []
    blueChampSup = []

    redChampTop = []
    redChampJug = []
    redChampMid = []   
    redChampBot = []
    redChampSup = []
    
    for i in range(len(allTeams)):
        if(i%3 == 0): blueTeam.append(allTeams[i])
        elif(i%3 == 1): redTeam.append(allTeams[i])
        else: winnerTeam.append(allTeams[i])

    for i in range(len(allPlayers)):
        if(i%10 == 0): bluePlayerTop.append(allPlayers[i])
        elif(i%10 == 1): bluePlayerJug.append(allPlayers[i])
        elif(i%10 == 2): bluePlayerMid.append(allPlayers[i])
        elif(i%10 == 3): bluePlayerBot.append(allPlayers[i])
        elif(i%10 == 4): bluePlayerSup.append(allPlayers[i])
        elif(i%10 == 5): redPlayerTop.append(allPlayers[i])
        elif(i%10 == 6): redPlayerJug.append(allPlayers[i])
        elif(i%10 == 7): redPlayerMid.append(allPlayers[i])
        elif(i%10 == 8): redPlayerBot.append(allPlayers[i])
        else: redPlayerSup.append(allPlayers[i])

    for i in range(len(allPicks)):
        if(i%10 == 0): blueChampTop.append(allPicks[i])
        elif(i%10 == 1): blueChampJug.append(allPicks[i])
        elif(i%10 == 2): blueChampMid.append(allPicks[i])
        elif(i%10 == 3): blueChampBot.append(allPicks[i])
        elif(i%10 == 4): blueChampSup.append(allPicks[i])
        elif(i%10 == 5): redChampTop.append(allPicks[i])
        elif(i%10 == 6): redChampJug.append(allPicks[i])
        elif(i%10 == 7): redChampMid.append(allPicks[i])
        elif(i%10 == 8): redChampBot.append(allPicks[i])
        else: redChampSup.append(allPicks[i])

    df = pd.DataFrame(list(zip(blueTeam, redTeam, winnerTeam, allWinSide, bluePlayerTop, 
    bluePlayerJug, bluePlayerMid, bluePlayerBot, bluePlayerSup, redPlayerTop, redPlayerJug, 
    redPlayerMid, redPlayerBot, redPlayerSup, blueChampTop, blueChampJug, blueChampMid, 
    blueChampBot, blueChampSup, redChampTop, redChampJug, redChampMid, redChampBot, redChampSup)), 
    columns =['blueTeam', 'redTeam', 'winnerTeam', 'winnerSide', 'bluePlayerTop', 'bluePlayerJug', 
    'bluePlayerMid', 'bluePlayerBot', 'bluePlayerSup', 'redPlayerTop',	'redPlayerJug', 'redPlayerMid',	
    'redPlayerBot',	'redPlayerSup', 'blueChampTop', 'blueChampJug', 'blueChampMid', 'blueChampBot', 
    'blueChampSup', 'redChampTop', 'redChampJug', 'redChampMid', 'redChampBot', 'redChampSup'])
    print(df)
    df.to_csv('lol_data.csv')

def allData(url):
    options = Options()
    options.add_argument("--headless=new")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--disk-cache-dir=/path/to/cache')
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    html = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(html, 'lxml')

    info = []
    # Format: [Blue, Red, Winner, Blue, Red, Winner, Blue ...]
    teamsList = scrapeTeams(soup) 
    # print(len(teamsList))
    # Format: [Blue1, Blue2, Blue3, Blue4,Blue5, Red1, Red2, Red3, Red4, Red5, Blue1 ...]
    playerList = scrapeRosters(soup)
    # print(len(playerList))
    # Format: [Blue1, Blue2, Blue3, Blue4,Blue5, Red1, Red2, Red3, Red4, Red5, Blue1 ...]
    picksList = scrapePicks(soup)
    # print(len(picksList))
    # Blue or Red
    winSideList = winnerSide(teamsList)
    # print(len(winSideList))

    info.append(teamsList)
    info.append(playerList)
    info.append(picksList)
    info.append(winSideList)

    return info


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
        name = player['data-to-id']
        if(name!="Zeka__28-Kim_Geon_2d-woo_29-" or playerList[-1]!="Zeka__28-Kim_Geon_2d-woo_29-"): 
            playerList.append(name)
        if(name=="Clid"): playerList.append("Zeka__28-Kim_Geon_2d-woo_29-")

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
    for i in range(len(teamsList)//3):
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
        

    # print(len(allPlayers))
    # print(allPlayers[-310:-290])
    # print(blueTeam[-5:])
    # print(redTeam[-5:])
    # print(winnerTeam[-5:])
    # print()
    # print()
    # print(bluePlayerTop[-5:])
    # print(bluePlayerJug[-5:])
    # print(bluePlayerMid[-5:])
    # print(bluePlayerBot[-5:])
    # print(bluePlayerSup[-5:])
    # print()
    # print()
    # print(redPlayerTop[-5:])
    # print(redPlayerJug[-5:])
    # print(redPlayerMid[-5:])
    # print(redPlayerBot[-5:])
    # print(redPlayerSup[-5:])
    # print()
    # print()
    # print(blueChampTop[-5:])
    # print(blueChampJug[-5:])
    # print(blueChampMid[-5:])
    # print(blueChampBot[-5:])
    # print(blueChampSup[-5:])
    # print()
    # print()
    # print(redChampTop[-5:])
    # print(redChampJug[-5:])
    # print(redChampMid[-5:])  
    # print(redChampBot[-5:])
    # print(redChampSup[-5:])

    # print(bluePlayerTop[0:5])
    # print(len(bluePlayerTop))
    # print(bluePlayerJug[0:5])
    # print(len(bluePlayerJug))
    # print(bluePlayerMid[0:5])
    # print(len(bluePlayerMid))
    # print(bluePlayerBot[0:5])
    # print(len(bluePlayerBot))
    # print(bluePlayerSup[0:5])
    # print(len(bluePlayerSup))

    # print()
    # print()
    
    # print(redPlayerTop[0:5])
    # print(len(redPlayerTop))
    # print(redPlayerJug[0:5])
    # print(len(redPlayerJug))
    # print(redPlayerMid[0:5])
    # print(len(redPlayerMid))
    # print(redPlayerBot[0:5])
    # print(len(redPlayerBot))
    # print(redPlayerSup[0:5])
    # print(len(redPlayerSup))

    # print()
    # print()

    # print(allWinSide[-30:])
    # print(len(allWinSide))




