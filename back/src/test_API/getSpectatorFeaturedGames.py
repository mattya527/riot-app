from riotwatcher import LolWatcher, ApiError
import os

# APIキーを設定
api_key = os.getenv('RIOT_API_KEY')
lol_watcher = LolWatcher(api_key)

platform = 'jp1'  # プラットフォームコードを適宜変更

try:
    # サモナー情報を取得
    # puuid = "QCCbUgKwomSanKMUNZQq5ui14SUmVUbFVeq6VLejUgVDFAuaOMnHbD9i2iMQzA0CFYpJyhboFRBE7g"
    res = lol_watcher.spectator.featured_games(region=platform)
    # active gameを取得
    print(res)

except ApiError as err:
    if err.response.status_code == 404:
        print('Active game not found.')
    else:
        raise