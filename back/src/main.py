from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.riotWatcherAccount import getPuuIdByRiotId
from modules.lolWatcherMatch import getMatchListByPuuId, getMatchByMatchId

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/getMatchHistory")
async def getMatchHistory(user_name : str ,tag_line : str, region : str = 'Asia'):
    response = []
    puuid = getPuuIdByRiotId(user_name, tag_line, region)
    print(puuid)
    if puuid == 'Riot accout not found.':
        return {"response" : "NG", "message" : "Riot accout not found."}
    match_list = getMatchListByPuuId(puuid, region)
    print(match_list)
    if match_list == 'Match list not found.':
        return {"response" : "NG", "message" : "Match list not found."}
    for match in match_list:
        print(match)
        match_info = getMatchByMatchId(match, region)
        response.append(match_info)
    return {"response" : "OK", "match_list" : response}
