from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import date
today = date.today()
d1 = today.strftime("%Y%m%d")
url = "https://www.espn.com/nba/scoreboard/_/date/" + d1
driver = webdriver.Chrome()
driver.get(url)
time.sleep(6)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"lxml")
games = []
thing1 = soup.find_all("div", class_ = "ScoreCell__TeamName ScoreCell__TeamName--abbev truncate db")
thing2 = soup.find_all("div", class_ = "ScoreCell__Score h9 clr-gray-01 fw-heavy tar")
thing3 = soup.find_all("div", class_ = "ScoreCell__Time h9 clr-negative")
thing3 = thing3 + soup.find_all("div", class_ = "ScoreCell__Time h9 clr-gray-01")
thing3 = thing3 +  soup.find_all("div", class_ = "ScoreCell__Time h9 clr-gray-03")
thing4 = soup.find_all("a", class_ = "ScoreCell__Link")
thing4 = thing4 + soup.find_all("a", class_ = "ScoreCell__CompetitorDetails")
for i in range(0,len(thing2),2):
    arr = {
        "home": thing1[i].get_text(), 
        "away": thing1[i+1].get_text(),
        "home-score": thing2[i].get_text(), 
        "away-score": thing2[i+1].get_text()
    }
    games.append(arr)
for i in range(len(thing2),len(thing1),2):
    arr = {
        "home": thing1[i].get_text(), 
        "away": thing1[i+1].get_text(),
        "home-score": "", 
        "away-score": ""
    }
    games.append(arr)
for i in range(len(thing3)):
    games[i]["game-status"]= thing3[i].get_text()
for i in range(len(thing4)):
    games[i]["link"] = "https://www.espn.com" + thing4[i]["href"]
url1 = "https://www.sofascore.com"
driver.get(url1)
time.sleep(5)
content1 = driver.page_source.encode('utf-8').strip()
soup1 = BeautifulSoup(content1,"lxml")
thing1 = soup1.find_all("div", class_ = "sc-hLBbgP eIlfTT")
thing2 = []
for i in range(len(thing1)):
    thing2.append(thing1[i]["title"])
    thing2[i] = thing2[i][:len(thing2[i])-11]
teamsIdWatch = ["Real Madrid", "Barcelona", "Bayern Munich", "Borussia Dortmund", "Paris Saint-Germain", "Manchester City", "Chelsea", "Arsenal", "Manchester United", "Tottenham"]
matches = []
for i in thing2:
    for j in teamsIdWatch:
        if(i.find(j) != -1):
            matches.append(i)
print(matches)