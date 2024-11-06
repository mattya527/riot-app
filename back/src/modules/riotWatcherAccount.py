from . import common

def getPuuIdByRiotId(user_name : str ,tag_line : str, region : str):    
    try:
        riot_account = common.riot_watcher.account.by_riot_id(region=region, game_name=user_name, tag_line=tag_line)
        return riot_account['puuid']
    except common.ApiError as err:
        if err.response.status_code == 404:
            return 'Riot accout not found.'
        else:
            raise