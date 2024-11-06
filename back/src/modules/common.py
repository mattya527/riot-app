from riotwatcher import LolWatcher, ApiError, RiotWatcher
import os

# APIキーを設定
api_key = os.getenv('RIOT_API_KEY')
lol_watcher = LolWatcher(api_key)
riot_watcher = RiotWatcher(api_key)
platform = 'jp1'  # プラットフォームコードを適宜変更
