from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.riotWatcherAccount import getPuuIdByRiotId
from modules.lolWatcherMatch import getMatchListByPuuId

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
    puuid = getPuuIdByRiotId(user_name, tag_line, region)
    print(puuid)
    if puuid == 'Riot accout not found.':
        return {"response" : "NG", "message" : "Riot accout not found."}
    match_list = getMatchListByPuuId(puuid, region)
    print(match_list)
    if match_list == 'Match list not found.':
        return {"response" : "NG", "message" : "Match list not found."}
    return {"response" : "OK", "match_list" : match_list}
