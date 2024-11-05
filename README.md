# RiotApp
## backend
APIキーは24時間で有効期限が消える
ホストのポートは8005番にフォワード
コンテナ内で
```
export RIOT_API_KEY={生成されたKEY}
```

```
pip3 install -r requirements.txt
```
## envfile
.docker.local.env
- RIOT_API_KEY="RIOT_API_KEY"

## frontend
npx create-react-appで作成
ホストのポートは3005番にフォワード