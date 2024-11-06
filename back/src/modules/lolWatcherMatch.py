from . import common

def getMatchListByPuuId(puuid : str, region : str):
    try:
        match_list = common.lol_watcher.match.matchlist_by_puuid(region=region, puuid=puuid)
        return match_list
    except common.ApiError as err:
        if err.response.status_code == 404:
            return 'Match list not found.'
        else:
            raise