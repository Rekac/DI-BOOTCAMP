import requests
import json
import os
from datetime import date, datetime
from zoneinfo import ZoneInfo

#this confirms my connection
def check_status(API_Key: str):
    url = "https://v3.football.api-sports.io/status"
    headers = {"x-apisports-key": API_Key}
    response = requests.get(url, headers=headers)
    data = response.json()
    current_status = data["response"]
    if isinstance(current_status, list): #resolves the issue with subscription being in a list
        current_status = current_status[0]
    plan = current_status["subscription"]["plan"]
    active = current_status["subscription"]["active"]
    used = current_status["requests"]["current"]
    limit = current_status["requests"]["limit_day"]
    remaining = limit - used
    print(f"Your account is {active} and you have {remaining} requests left for today.")
My_Key = "55a9b5f4b712ee18c2b49c2531bfb12b".strip()
check_status(My_Key)
# #get a list of parameters from the "Fixtures" endpoint
# def get_parameters(API_Key: str):
#     url = "https://v3.football.api-sports.io/"
#     headers = {"x-apisports-key": API_Key}
#     response = requests.get(url, headers=headers, params={"next": 5})
#     data = response.json()
#     fixtures = data["response"]
#     if not fixtures:
#         print("No fixtures found.")
#         return
#     initial = fixtures[0]
#     print(sorted(initial.keys()))
# My_Key = "55a9b5f4b712ee18c2b49c2531bfb12b".strip()
# get_parameters(My_Key)
#get API and put into JSON file
def get_data(API_Key: str, filename="footballdata.json", timezone: str = "Europe/Vienna", upcoming: bool = True, limit: int= 50, tonight_only: bool = False, start_hour: int = 18, end_hour: int = 23):
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {"x-apisports-key": API_Key}
    params = {
        "date": date.today().isoformat(),
        "timezone": timezone}
    if upcoming:
        params["status"] = "NS"
    response = requests.get(url, headers=headers, params=params, timeout=15)
    data = response.json() #pulls API data into the JSON file
    fixtures = data.get("response", [])
    print("API errors:", data.get("errors"))
    print("API echoed params:", data.get("parameters"))
#after work option
    if tonight_only:
        fixtures = [
            f for f in fixtures
            if start_hour <= int(f["fixture"]["date"][11:13]) <= end_hour
        ]
    #get all matches by kickoff start time
    fixtures.sort(key=lambda f: f["fixture"]["date"])
    if limit:
        fixtures = fixtures[:limit]
    data["response"] = fixtures
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(fixtures)} fixtures to {filename}.")
    #print it nicely
   for f in fixtures:
    timestamp = f["fixture"]["timestamp"]
    timezone  = f["fixture"]["timezone"]
    dt = datetime.fromtimestamp(timestamp, ZoneInfo(timezone))
    # 12-hour format like "8PM" or "8:30PM"
    if dt.minute == 0:
        tstr = dt.strftime("%d/%m/%Y %H:%M:%S")
    else:
        tstr = dt.strftime("%H:%M")
        Date = dt.strftime("%d/%m/%Y")
        league = f["league"]["name"]   
        logo_league = f["league"]["logo"]    
        country = f["league"]["country"] 
        local =f["fixture"]["venue"]           
        home = f["teams"]["home"]["name"]
        logo_home = f["teams"]["home"]["logo"]
        away = f["teams"]["away"]["name"]
        logo_away=f["teams"]["away"]["logo"]
        score_home=f["score"]["fulltime"]["home"]
        score_away=f["score"]["fulltime"]["away"]     
        name_Competion=f["competition"]["name"]
        emblem_Competitio=f["competition"]["type"]

        
        print(f"{Date}  {tstr}  : {country} {logo_league} {league} {logo_home} {home} {score_home}vs{score_Aaway}   {logo_away} {away} ")
My_Key = "55a9b5f4b712ee18c2b49c2531bfb12b".strip()
#get_data(My_Key, upcoming=False)
get_data(My_Key, upcoming=False)  # include live/finished too


