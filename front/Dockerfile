FROM node:20-alpine

# 必要な環境変数を設定
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
ENV LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja
ENV NODE_OPTIONS=--openssl-legacy-provider

RUN apk add openssl
WORKDIR /src
# RUN npm install