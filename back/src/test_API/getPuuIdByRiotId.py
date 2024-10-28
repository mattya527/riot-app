from riotwatcher import LolWatcher, ApiError, RiotWatcher
import os

# APIキーを設定
api_key = os.getenv('RIOT_API_KEY')
lol_watcher = LolWatcher(api_key)
riot_watcher = RiotWatcher(api_key)

# サモナー名とリージョンを設定
summoner_name = 'Mattya'
tag_line = 'JP2'
region = 'Asia'  # リージョンコードを適宜変更
platform = 'jp1'  # プラットフォームコードを適宜変更

try:
    # サモナー情報を取得
    riot_account = riot_watcher.account.by_riot_id(region=region, game_name=summoner_name, tag_line=tag_line)
    print(riot_account)
    # PUUIDを取得
    puuid = riot_account['puuid']
    print(f"PUUID: {puuid}")

except ApiError as err:
    if err.response.status_code == 404:
        print('Riot accout not found.')
    else:
        raise