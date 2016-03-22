#http://lol.esportspedia.com/wiki/League_Championship_Series/North_America/2016_Season/Spring_Season/Scoreboards/Week_2
#This file should be given the webpage and should return the pick order
import urllib.request
from bs4 import BeautifulSoup
def Main(URL):
    NewURL,weeknum = Convert_URL(URL)
    webpage = Get_Page_As_BS4(NewURL)
    PicksnBansObject = Get_Picks_And_Bans(webpage,weeknum)
    return PicksnBansObject
def Convert_URL (URL):
    """ This will convert the URL to the URL to retrieve data for Picks."""
    if "Scoreboards" in URL:
        tmpURL = URL.split("/")
        lentmpURL = len(tmpURL)
        try:
            weeknum = int((tmpURL[lentmpURL-1]).split("_")[1])
        except:
            weeknum = 0
        URL = ""
        if "Week" in tmpURL[lentmpURL-1]:
            spot = 2
        else:
            spot = 1
        for i in range(lentmpURL-spot):

            URL += (tmpURL[i]+"/")
        URL +=("Picks_and_Bans")
    return URL,weeknum
def Get_Page_As_BS4(URL):
    with urllib.request.urlopen(URL) as webpage:
        content = webpage.read()
    soup = BeautifulSoup(content,"html.parser")
    return soup
def Get_Picks_And_Bans(webpage,weeknum):
    GameList = []
    bodyContent = webpage.find(id="bodyContent")
    mwcontenttext = bodyContent.find(id="mw-content-text")
    if weeknum == 0:
        pmbct = mwcontenttext.find(style="padding:0; margin:0;background-color:transparent;")
    else:
        pmbct = mwcontenttext.find_all(style="padding:0; margin:0;background-color:transparent;")
        pmbct = pmbct[weeknum-1]
    td = pmbct.find('td')
    div = td.find_all('div',style="display: inline-block;vertical-align:top;padding-right:1em;")
    count = 1
    for game in div:
        count += 1
        GameObject = {'Game Name': None,
                      'BTeam': None,
                      'RTeam': None}
        BTeamGameObject = {'Team Name': None,
                      'Team Bans': [],
                      'Team Picks': [],
                      'Team Picks Pos': []}
        RTeamGameObject = {'Team Name': None,
                      'Team Bans': [],
                      'Team Picks': [],
                      'Team Picks Pos': []}
        trs = game.find_all('tr')
        #Compile Blue Team Data
        try:
            BTeamGameObject['Team Name'] = trs[1].find_all('a')[0]['title'].strip()
        except:
            BTeamGameObject['Team Name'] = "No Data"
        BTeamGameObject['Team Bans'].append(trs[3].find_all('td')[0].get_text().strip())
        if BTeamGameObject['Team Bans'][0] == "":
            BTeamGameObject['Team Bans'][0] = ("No Data")
        BTeamGameObject['Team Bans'].append(trs[4].find_all('td')[0].get_text().strip())
        if BTeamGameObject['Team Bans'][1] == "":
            BTeamGameObject['Team Bans'][1] = ("No Data")
        BTeamGameObject['Team Bans'].append(trs[5].find_all('td')[0].get_text().strip())
        if BTeamGameObject['Team Bans'][2] == "":
            BTeamGameObject['Team Bans'][2] = ("No Data")
        try:
            BTeamGameObject['Team Picks'].append(trs[6].find_all('td')[0].find('a')['title'].strip())
        except:
            BTeamGameObject['Team Picks'].append("No Data")
        try:
            BTeamGameObject['Team Picks Pos'].append(trs[6].find_all('td')[1].find('span')['title'].strip())
        except:
            BTeamGameObject['Team Picks Pos'].append("No Data")
        try:
            BTeamGameObject['Team Picks'].append(trs[7].find_all('td')[0].find('a')['title'].strip())
        except:
            BTeamGameObject['Team Picks'].append("No Data")
        try:
            BTeamGameObject['Team Picks Pos'].append(trs[7].find_all('td')[1].find('span')['title'].strip())
        except:
            BTeamGameObject['Team Picks Pos'].append("No Data")
        try:
            BTeamGameObject['Team Picks'].append(trs[8].find_all('td')[0].find('a')['title'].strip())
        except:
            BTeamGameObject['Team Picks'].append("No Data")
        try:
            BTeamGameObject['Team Picks Pos'].append(trs[8].find_all('td')[1].find('span')['title'].strip())
        except:
            BTeamGameObject['Team Picks Pos'].append("No Data")
        try:
            BTeamGameObject['Team Picks'].append(trs[9].find_all('td')[0].find('a')['title'].strip())
        except:
            BTeamGameObject['Team Picks'].append("No Data")
        try:
            BTeamGameObject['Team Picks Pos'].append(trs[9].find_all('td')[1].find('span')['title'].strip())
        except:
            BTeamGameObject['Team Picks Pos'].append("No Data")
        try:
            BTeamGameObject['Team Picks'].append(trs[10].find_all('td')[0].find('a')['title'].strip())
        except:
            BTeamGameObject['Team Picks'].append("No Data")
        try:
            BTeamGameObject['Team Picks Pos'].append(trs[10].find_all('td')[1].find('span')['title'].strip())
        except:
            BTeamGameObject['Team Picks Pos'].append("No Data")
        #Compile Red Team Data
        try:
            RTeamGameObject['Team Name'] = trs[1].find_all('a')[1]['title'].strip()
        except:
            RTeamGameObject['Team Name'] = "No Data"
        RTeamGameObject['Team Bans'].append(trs[3].find_all('td')[0].get_text().strip())
        if RTeamGameObject['Team Bans'][0] == "":
            RTeamGameObject['Team Bans'][0] = ("No Data")
        RTeamGameObject['Team Bans'].append(trs[4].find_all('td')[0].get_text().strip())
        if RTeamGameObject['Team Bans'][1] == "":
            RTeamGameObject['Team Bans'][1] = ("No Data")
        RTeamGameObject['Team Bans'].append(trs[5].find_all('td')[0].get_text().strip())
        if RTeamGameObject['Team Bans'][2] == "":
            RTeamGameObject['Team Bans'][2] = ("No Data")
        try:
            RTeamGameObject['Team Picks'].append(trs[6].find_all('td')[0].find('a')['title'].strip())
        except:
            RTeamGameObject['Team Picks'].append("No Data")
        try:
            RTeamGameObject['Team Picks Pos'].append(trs[6].find_all('td')[1].find('span')['title'].strip())
        except:
            RTeamGameObject['Team Picks Pos'].append("No Data")
        try:
            RTeamGameObject['Team Picks'].append(trs[7].find_all('td')[0].find('a')['title'].strip())
        except:
            RTeamGameObject['Team Picks'].append("No Data")
        try:
            RTeamGameObject['Team Picks Pos'].append(trs[7].find_all('td')[1].find('span')['title'].strip())
        except:
            RTeamGameObject['Team Picks Pos'].append("No Data")
        try:
            RTeamGameObject['Team Picks'].append(trs[8].find_all('td')[0].find('a')['title'].strip())
        except:
            RTeamGameObject['Team Picks'].append("No Data")
        try:
            RTeamGameObject['Team Picks Pos'].append(trs[8].find_all('td')[1].find('span')['title'].strip())
        except:
            RTeamGameObject['Team Picks Pos'].append("No Data")
        try:
            RTeamGameObject['Team Picks'].append(trs[9].find_all('td')[0].find('a')['title'].strip())
        except:
            RTeamGameObject['Team Picks'].append("No Data")
        try:
            RTeamGameObject['Team Picks Pos'].append(trs[9].find_all('td')[1].find('span')['title'].strip())
        except:
            RTeamGameObject['Team Picks Pos'].append("No Data")
        try:
            RTeamGameObject['Team Picks'].append(trs[10].find_all('td')[0].find('a')['title'].strip())
        except:
            RTeamGameObject['Team Picks'].append("No Data")
        try:
            RTeamGameObject['Team Picks Pos'].append(trs[10].find_all('td')[1].find('span')['title'].strip())
        except:
            RTeamGameObject['Team Picks Pos'].append("No Data")

        GameObject['BTeam'] = BTeamGameObject
        GameObject['RTeam'] = RTeamGameObject
        GameObject['Game Name'] = GameObject['BTeam']['Team Name']+" vs "+GameObject['RTeam']['Team Name']
        GameList.append(GameObject)
    return GameList