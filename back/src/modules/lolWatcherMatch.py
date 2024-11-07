from . import common

# 該当ユーザーの対戦履歴をcount分取得
def getMatchListByPuuId(puuid : str, region : str):
    try:
        match_list = common.lol_watcher.match.matchlist_by_puuid(region=region, puuid=puuid,count=1)
        return match_list
    except common.ApiError as err:
        if err.response.status_code == 404:
            return 'Match list not found.'
        else:
            raise

# puuidと該当マッチIDから試合情報を取得してリスト表示に必要なものだけ成形して返却する  
def getMatchOutlineByMatchIdAndPuuId(matchid : str , puuid : str, region : str):
    try:
        response = {}
        match = common.lol_watcher.match.by_id(region=region, match_id=matchid)
        response["matchId"] = match["metadata"]["matchId"]
        response["gameCreation"] = match["info"]["gameCreation"] # ロード画面からの時間
        response["gameDuration"] = match["info"]["gameDuration"]
        response["gameEndTimestamp"] = match["info"]["gameEndTimestamp"]
        response["gameMode"] = match["info"]["gameMode"]
        response["gameStartTimestamp"] = match["info"]["gameStartTimestamp"]
        response["gameType"] = match["info"]["gameType"]
        response["gameVersion"] = match["info"]["gameVersion"]
        response["mapId"] = match["info"]["mapId"]
        response["participants"] = match["info"]["participants"]
        response["queueId"] = match["info"]["queueId"]
        response["teams"] = match["info"]["teams"]
        
        index = next(i for i, participant in enumerate(match["info"]["participants"]) if participant["puuid"] == puuid)
        print(index)
        response["target_user"] = match["info"]["participants"][index]
        
        return response
    except common.ApiError as err:
        if err.response.status_code == 404:
            return 'Match not found.'
        else:
            raise