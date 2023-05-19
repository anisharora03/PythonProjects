from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import unidecode
import random
import time
import json
def players(teams, years, driver):
    for t in teams:
        for y in years:
            url = "https://www.baseball-reference.com/teams/" + t[0] + "/" + y + ".shtml"
            driver.get(url)
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"html.parser")
            dr = 0
            pa = 11
            while pa > 10:
                if (not soup.find("tr" , {"data-row": str(dr)}).has_attr("class") or soup.find("tr" , {"data-row": str(dr)})["class"][0] != "thead"):
                    name = soup.find("tr" , {"data-row": str(dr)}).find("td", {"data-stat":"player"}).find("a").get_text()
                    pa = int(soup.find("tr" , {"data-row": str(dr)}).find("td", {"data-stat":"PA"}).get_text())
                    thing = {"first_name": unidecode.unidecode(bytes(name.split()[0], 'utf-8').decode()),
                            "last_name" : unidecode.unidecode(bytes(name[name.index(" ") + 1:], 'utf-8').decode()),
                            "year" : y,
                            "pa": str(pa)}
                    print(thing)
                    t.append(thing)
                dr += 1
            t.pop(-1)
            time.sleep(2.0 + random.random() * 3)
    return t
def teams(teams, years, driver):
    wp = []
    for t in teams:
        for y in range(len(years)):
            url = "https://www.baseball-reference.com/teams/" + t[0]
            driver.get(url)
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"html.parser")
            thing = {
                "year": years[-y - 1],
                "team": t,
                "wp": soup.find("div", id = "div_franchise_years").find("tr" , {"data-row": str(y)}).find("td", {"data-stat" : "R"}).get_text()
            }
            wp.append(thing)
        time.sleep(2.0 + random.random() * 3)
def files(wp, teams):
    with open("teams.json", "w") as outfile:
        json.dump(wp, outfile)

    with open("players.json", "w") as outfile:
        json.dump(teams, outfile)
if __name__ == '__main__':
    teams = [["LAA"], ["ARI"], ["ATL"], ["BAL"], ["BOS"], ["CHC"], ["CHW"], ["CIN"], ["CLE"], ["COL"], ["DET"], ["MIA"]
         , ["HOU"], ["KCR"], ["LAD"], ["MIL"], ["MIN"], ["NYM"], ["NYY"], ["OAK"], ["PHI"], ["PIT"],["SDP"]
         , ["SEA"], ["SFG"], ["STL"], ["TBR"], ["TEX"], ["TOR"], ["WSN"]]
    years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options = options)
    team = players(teams, years, driver)
    wp = teams(teams, years, driver)
    files(wp, team)
    driver.quit()
'''
for t in teams:
    for y in years:
        url = "https://www.baseball-reference.com/teams/" + t[0] + "/" + y + ".shtml"
        driver.get(url)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"html.parser")
        action = webdriver.ActionChains(driver)
        element = driver.find_element(By.XPATH, "//*[@id='team_batting']/thead/tr/th[6]")
        action.move_to_element_with_offset(element, 5, 20).click()
        i = 0
        print(soup.find("tr" , {"data-row": str(0)}).find("td", {"data-stat":"player"}).find("a").get_text())
        print(soup.find("div", id = "div_team_batting").find("tbody").find("tr"))
        pa = 11
        while pa > 10:
            name = soup.find("tbody").name.contents[i]
            pa = int(soup.find("tr" , {"data-row": str(i)}).find("td", {"data-stat":"PA"}).get_text())
            thing = {"first_name": unidecode.unidecode(bytes(name.split()[0], 'utf-8').decode()),
                        "last_name" : unidecode.unidecode(bytes(name.split()[1], 'utf-8').decode()),
                        "year" : y,
                        "pa": str(pa)}
            print(thing)
            i += 1
driver.quit()
'''
