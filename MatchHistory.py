import urllib.request
key="b6cee542-fc7a-4501-91ce-e65292b99494"
CoreURL = "https://na.api.pvp.net/api/lol/"
EndURL = "?api_key="+key

def Build_MatchURL(region,matchid):
    global CoreURL, EndURL
    URL = CoreURL+str(region)+"/v2.2/match/"+str(matchid)+EndURL
    #URL = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/RiotSchmick?api_key="+key
    print (URL)
    with urllib.request.urlopen(URL) as webpage:
        content = webpage.read()
    return content




region="na"
matchid="1842343823"
print(Build_MatchURL(region,matchid))
