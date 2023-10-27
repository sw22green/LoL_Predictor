from requests_html import HTMLSession
from bs4 import BeautifulSoup
import csv
import pandas as pd
from itertools import chain

class DataScraper:
    def __init__(self):
        self.session = HTMLSession()

    def fetch_data(self, url):
        response = self.session.get(url)
        html = response.html.html
        soup = BeautifulSoup(html, 'lxml')

        teamsList = self.scrape_teams(soup)
        playerList = self.scrape_rosters(soup)
        picksList = self.scrape_picks(soup)
        winSideList = self.winner_side(teamsList)

        return teamsList, playerList, picksList, winSideList

    def scrape_teams(self, soup):
        teamsList = []

        teamElement = soup.find_all(class_="mhgame-result")
        for teamData in teamElement:
            imgElement = teamData.find('img')

            if imgElement:
                teamName = imgElement.get('alt')[:-8]
                teamsList.append(teamName) 
        return teamsList

    def scrape_rosters(self, soup):
        playerList = []

        playerElement = soup.find_all('a', class_=["catlink-players pWAG pWAN", "mw-redirect"])

        for playerData in playerElement:
            playerName = playerData.get_text(strip=True)
            playerList.append(playerName)
        return playerList

    def scrape_picks(self, soup):
        picksList = []
        count = 0

        picksElement = soup.find_all(class_="sprite champion-sprite")
        for picksData in picksElement:
            champPicked = picksData.get('title')
            if (count % 20 > 9):
                picksList.append(champPicked)
            count += 1
        return picksList

    def winner_side(self, teamsList):
        winSideList = []
        for i in range(len(teamsList) // 3):
            if (teamsList[3 * (i + 1) - 1] == (teamsList[3 * (i + 1) - 2])):
                winSideList.append("Red")
            else:
                winSideList.append("Blue")
        return winSideList

class DataProcessor:
    def process_data(self, url_list):
        allTeams = []
        allPlayers = []
        allPicks = []
        allWinSide = []

        scraper = DataScraper()

        for url in url_list:
            info = scraper.fetch_data(url)
            allTeams.append(info[0])
            allPlayers.append(info[1])
            allPicks.append(info[2])
            allWinSide.append(info[3])

        allTeams = list(chain.from_iterable(allTeams))
        allPlayers = list(chain.from_iterable(allPlayers))
        allPicks = list(chain.from_iterable(allPicks))
        allWinSide = list(chain.from_iterable(allWinSide))

        # Data processing code

        df = pd.DataFrame(list(zip(allTeams)), columns=['Teams'])
        # Add the other columns to the DataFrame
        df.to_csv('lol_data.csv')



        

def main():
    url_list = ["https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Btournament%5D=LCK%2F2023+Season%2FSpring+Season&MHG%5Blimit%5D=500&MHG%5Bpreload%5D=Tournament&MHG%5Bspl%5D=yes&_run=",
                "https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Tournament&MHG%5Btournament%5D=LCK%2F2023+Season%2FSpring+Playoffs&_run=",
                "https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Btournament%5D=LCK%2F2023+Season%2FSummer+Season&MHG%5Blimit%5D=500&MHG%5Bpreload%5D=Tournament&MHG%5Bspl%5D=yes&_run=",
                "https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Tournament&MHG%5Btournament%5D=LCK%2F2023+Season%2FSummer+Playoffs&_run="]

    processor = DataProcessor()
    processor.process_data(url_list)

if __name__ == "__main__":
    main()
