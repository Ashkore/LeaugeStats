import urllib.request
import PickOrder
from datetime import datetime
from bs4 import BeautifulSoup
from Excel import Write_ToExcel
def Parse_Days(Days):
    """Splits the html up so that each day can be parsed."""
    DaysObject = []
    for Day in range(len(Days)):
        Games = Days[Day].find_all(style="display: inline-block;vertical-align:top;")
        GamesObject = Parse_Games(Games)
        DaysObject.append(GamesObject)
    return DaysObject
def Parse_Games(Games):
    """Splits the html up so that each game can be parsed."""
    GamesObject = []
    for Game in range(len(Games)):
        GameObject = {'Game Title': None, #I have this data
              'Game Number': None, #I have this data
              'Links': None,
              'Blue Team Info': None, #I have this data
              'Blue Team Char Info': None, #I have this data
              'Red Team Info': None, #I have this data
              'Red Team Char Info': None, #I have this data
              'Game Length': None} #I have this data
        if '</td>' not in (str(Games[Game])):
            continue
        #Set GameTitle
        GameObject['Game Title'] = Parse_GameTitle(Games[Game])
        #Centralize Area
        GameInfoArea = Games[Game].find(class_='wikitable matchrecap1')
        GameInfoSections = GameInfoArea.find_all('tr')
        #Set GameNumber
        GameObject['Game Number'] = ((GameInfoSections[0].get_text()).split("  ")[0]).strip()
        GameObject['Blue Team Info'],GameObject['Red Team Info'],GameObject['Game Length'] = Parse_GenGameInfo(GameInfoSections[1],GameObject['Game Title'])
        GameObject['Blue Team Char Info'] = Parse_CharInfo(GameInfoSections[8])#TeamBlue
        GameObject['Red Team Char Info'] = Parse_CharInfo(GameInfoSections[20])#TeamRed
        GameObject['Links'] = Parse_Links(GameInfoSections[32].find_all('td'))
        GamesObject.append(GameObject)
    return GamesObject
def Parse_GameTitle(Game):
    """Returns the title of the game. EX: Team Blue vs Team Red"""
    Names = Game.find_all('div')
    GameTitle = (Names[1].get_text().strip()+" ")+(Names[2].get_text().strip().replace(".","")+" ")+(Names[3].get_text().strip())
    return GameTitle
def Parse_GenGameInfo(GenGameInfo,GameTitle):
    """Return each teams info."""
    RedTeamObject = {'Win': None, #I have this data
                     'Gold': None, #I have this data
                     'Kills': None, #I have this data
                     'Deaths':None,
                     'Towers': None, #I have this data
                     'Dragons': None, #I have this data
                     'Barons': None,
                     'Picks': None,
                     'Picks Pos': None,
                     'Bans': None} #I have this data
    BlueTeamObject = {'Win': None, #I have this data
                     'Gold': None, #I have this data
                     'Kills': None, #I have this data
                     'Deahts':None,
                     'Towers': None, #I have this data
                     'Dragons': None, #I have this data
                     'Barons': None,
                     'Picks': None,
                     'Picks Pos': None,
                     'Bans': None} #I have this data
    GoldRow = GenGameInfo.find_all('tr')[3].find_all('td')
    #####     WINS     #####
    if((GenGameInfo.find_all(class_="matchrecapScoreLine"))[1].get_text()).strip() == "1":
         BlueTeamObject['Win'] = str(True)
    else:
         BlueTeamObject['Win'] = str(False)
    if ((GenGameInfo.find_all(class_="matchrecapScoreLine"))[2].get_text()).strip() == "1":
        RedTeamObject['Win'] = str(True)
    else:
        RedTeamObject['Win'] = str(False)
    #####     GOLD     #####
    if "." in (GoldRow[0].get_text()).strip():
        BlueTeamObject['Gold'] = (GoldRow[0].get_text()).strip().replace(".","").replace("k","00")
    else:
        BlueTeamObject['Gold'] = "Error Parsing Data"
    if "." in (GoldRow[0].get_text()).strip():
        RedTeamObject['Gold'] = (GoldRow[10].get_text()).strip().replace(".","").replace("k","00")
    else:
        RedTeamObject['Gold'] = "Error Parsing Data"
    #####     TOTAL KILLS     #####
    BlueTeamObject['Kills'] = (GoldRow[1].get_text()).strip()
    RedTeamObject['Kills'] = (GoldRow[9].get_text()).strip()
    #####     TOWERS     #####
    BlueTeamObject['Towers'] = (GoldRow[2].get_text()).strip()
    RedTeamObject['Towers'] = (GoldRow[8].get_text()).strip()
    #####     DRAGONS     #####
    BlueTeamObject['Dragons'] = (GoldRow[3].get_text()).strip()
    RedTeamObject['Dragons'] = (GoldRow[7].get_text()).strip()
    #####     BARONS     #####
    BlueTeamObject['Barons'] = (GoldRow[4].get_text()).strip()
    RedTeamObject['Barons'] = (GoldRow[6].get_text()).strip()
    #####     GAME TIME     #####
    TotalGameTime = GoldRow[5].get_text().strip()
    TotalGameTime = TotalGameTime.split(":")
    if len(TotalGameTime) == 2:
        Mins = TotalGameTime[0]
        Secs = TotalGameTime[1]
        TotalGameTime = (int(Mins)*60)+int(Secs)
        TotalGameTime = str(TotalGameTime)
    elif len(TotalGameTime) == 3: #If Game Last over an Hour
        Hours = TotalGameTime[0]
        Mins = TotalGameTime[0]
        Secs = TotalGameTime[1]
        TotalGameTime = ((int(Hours)*60)*60)+(int(Mins)*60)+int(Secs)
        TotalGameTime = str(TotalGameTime)
    else:
        TotalGameTime = "Error Parsing Game Time"
    return BlueTeamObject,RedTeamObject,TotalGameTime
def Parse_CharInfo(TeamCharInfo):
    """Returns all thecharacters of a team and their information."""
    CharsObject = {'CharOne': None, #I have this data
                   'CharTwo': None, #I have this data
                   'CharThree': None, #I have this data
                   'CharFour': None, #I have this data
                   'CharFive': None, #I have this data
                   }
    CharsObject['CharOne'] = Parse_IndividualChar(TeamCharInfo.find_all('tr')[0])
    CharsObject['CharTwo'] = Parse_IndividualChar(TeamCharInfo.find_all('tr')[2])
    CharsObject['CharThree'] = Parse_IndividualChar(TeamCharInfo.find_all('tr')[4])
    CharsObject['CharFour'] = Parse_IndividualChar(TeamCharInfo.find_all('tr')[6])
    CharsObject['CharFive'] = Parse_IndividualChar(TeamCharInfo.find_all('tr')[8])
    return CharsObject
def Parse_IndividualChar(Char):
    """Returns the individual attributes of a character."""
    CharObject = ['Name','Champ','SS One','SS Two','Kills','Deaths','Assists','CS','Gold','Items','Trinket','Mastery']
    A = Char.find(class_="prettytable")
    GoldInt = 10
    CSInt = 11
    CharObject[0] = (A.find_all('td')[1].get_text()).strip()            #Name
    CharObject[1] = (A.find_all('td')[0].find('a')['title']).strip()    #Champ
    CharObject[2] = (A.find_all('td')[2].find('a')['title']).strip()    #SS One
    CharObject[3] = (A.find_all('td')[3].find('a')['title']).strip()    #SS Two
    CharObject[4] = (A.find_all('td')[5].get_text()).strip()           #Kills
    CharObject[5] = (A.find_all('td')[6].get_text()).strip()         #Deaths
    CharObject[6] = (A.find_all('td')[7].get_text()).strip()            #Assists
    CharObject[7] = (A.find_all('td')[11].get_text()).strip()          #CS
    if "." in (A.find_all('td')[10].get_text()).strip():
        CharObject[8] = (A.find_all('td')[10].get_text()).strip().replace(".","").replace("k","00") #Gold
    else:
        CharObject[8] = "Error Parsing Data"                            #Gold
    CharObject[9] = Parse_Itemsfromlist(A.find_all('td')[8])            #Items
    CharObject[10] = (A.find_all('td')[9].find('a')['title']).strip()   #Trinket
    CharObject[11] = (A.find_all('td')[4].find('a')['title']).strip()   #Mastery
    return CharObject
def Parse_Itemsfromlist(Object):
    """Returns a list of 6 items. If the character did not have 6 items then the word "None" will be the place holder"""
    InformationObject = []
    Items = Object.find_all('a')
    for item in range(len(Items)):
        InformationObject.append((Items[item]['title']).strip())
    while len(InformationObject) != 6:
        InformationObject.append("None")
    return InformationObject
def Parse_Links(Object):
    """Returns an object of two links, the video link and match history link. If one is not present then object will be nulled."""
    InformationObject = {'Video': None,
                         'Match History': None}
    links = Object[5].find_all('a')
    try:
        InformationObject['Video'] = links[0]['href']
    except:
        InformationObject['Video'] = None
    try:
        InformationObject['Match History'] = links[1]['href']
    except:
        InformationObject['Match History'] = None
    return InformationObject
def Add_Picks_And_Bans_To_Data(Data,PnBs):
    for PnB in PnBs:
        for Games in Data:
            for Game in Games:
                if Game['Game Title'] == PnB['Game Name']:
                    Game['Red Team Info']['Bans'] = PnB['RTeam']['Team Bans']
                    Game['Red Team Info']['Picks'] = PnB['RTeam']['Team Picks']
                    Game['Red Team Info']['Picks Pos'] = PnB['RTeam']['Team Picks Pos']
                    Game['Blue Team Info']['Bans'] = PnB['BTeam']['Team Bans']
                    Game['Blue Team Info']['Picks'] =  PnB['BTeam']['Team Picks']
                    Game['Blue Team Info']['Picks Pos'] =  PnB['BTeam']['Team Picks Pos']
    return Data
def Add_Percent_To_Data(Data):
    for Game in Data:
        for Info in Game:
            RedTeam = Info['Red Team Char Info']
            BlueTeam = Info['Blue Team Char Info']
            BteamGold = 0
            BteamAssists = 0
            BteamKills = 0
            BteamDeaths = 0
            BteamCS = 0
            RteamGold = 0
            RteamAssists = 0
            RteamKills = 0
            RteamDeaths = 0
            RteamCS = 0
            for Char in BlueTeam:
                BteamGold += int(BlueTeam[Char][8])
                BteamAssists += int(BlueTeam[Char][6])
                BteamKills += int(BlueTeam[Char][4])
                BteamDeaths += int(BlueTeam[Char][5])
                BteamCS += int(BlueTeam[Char][7])
            Info['Blue Team Info']['Deaths'] = str(BteamDeaths)
            for Char in RedTeam:
                RteamGold += int(RedTeam[Char][8])
                RteamAssists += int(RedTeam[Char][6])
                RteamKills += int(RedTeam[Char][4])
                RteamDeaths += int(RedTeam[Char][5])
                RteamCS += int(RedTeam[Char][7])
            Info['Red Team Info']['Deaths'] = str(RteamDeaths)
            for Char in BlueTeam:
                if BteamGold != 0:
                    BlueTeam[Char].insert(9,(str(round((int(BlueTeam[Char][8])/BteamGold)*100))))
                else:
                    BlueTeam[Char].insert(9,0)
                if BteamCS != 0:
                    BlueTeam[Char].insert(8,(str(round((int(BlueTeam[Char][7])/BteamCS)*100))))
                else:
                    BlueTeam[Char].insert(8,0)
                if BteamAssists != 0 :
                    BlueTeam[Char].insert(7,(str(round((int(BlueTeam[Char][6])/BteamAssists)*100))))
                else:
                    BlueTeam[Char].insert(7,0)
                if BteamDeaths != 0:
                    BlueTeam[Char].insert(6,(str(round((int(BlueTeam[Char][5])/BteamDeaths)*100))))
                else:
                    BlueTeam[Char].insert(6,0)
                if BteamKills != 0:
                    BlueTeam[Char].insert(5,(str(round((int(BlueTeam[Char][4])/BteamKills)*100))))
                else:
                    BlueTeam[Char].insert(5,0)
            for Char in RedTeam:
                if RteamGold != 0:
                    RedTeam[Char].insert(9,(str(round((int(RedTeam[Char][8])/RteamGold)*100))))
                else:
                    RedTeam[Char].insert(9,0)
                if RteamCS != 0:
                    RedTeam[Char].insert(8,(str(round((int(RedTeam[Char][7])/RteamCS)*100))))
                else:
                    RedTeam[Char].insert(8,0)
                if RteamAssists != 0:
                    RedTeam[Char].insert(7,(str(round((int(RedTeam[Char][6])/RteamAssists)*100))))
                else:
                    RedTeam[Char].insert(7,0)
                if RteamDeaths != 0:
                    RedTeam[Char].insert(6,(str(round((int(RedTeam[Char][5])/RteamDeaths)*100))))
                else:
                    RedTeam[Char].insert(6,0)
                if RteamKills != 0:
                    RedTeam[Char].insert(5,(str(round((int(RedTeam[Char][4])/RteamKills)*100))))
                else:
                    RedTeam[Char].insert(5,0)

    return Data

def Main(URL,FileName):
    if URL[-1] == "/":
        URL = URL[0:len(URL)-1]
    with urllib.request.urlopen(URL) as webpage:
        content = webpage.read()
    soup = BeautifulSoup(content,"html.parser")
    Main = soup.find(id="mw-content-text",class_="mw-content-ltr")
    Days = Main.find_all(style="padding:0; margin:0;background-color:transparent;")
    Data = Parse_Days(Days)#Get the data
    PicksAndBans = PickOrder.Main(URL)
    Data1 = Add_Picks_And_Bans_To_Data(Data,PicksAndBans)
    Data2 = Add_Percent_To_Data(Data1)
    Write_ToExcel(Data2,FileName)#Write the data to an excel file






