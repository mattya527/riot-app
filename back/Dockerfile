FROM ubuntu:24.04

# 必要な環境変数を設定
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHON_VERSION=3.12.6
ENV TZ=Asia/Tokyo
ENV LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja

# Pythonに必要なパッケージのインストール
RUN apt update && apt upgrade -y && \
    apt install -y wget curl build-essential libbz2-dev libdb-dev \
    libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
    libncursesw5-dev libsqlite3-dev libssl-dev \
    zlib1g-dev uuid-dev \
    && rm -rf /var/lib/apt/lists/*

# Pythonのインストール
RUN wget -P /tmp https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && tar zxvf /tmp/Python-${PYTHON_VERSION}.tgz -C /tmp/ && \
    cd /tmp/Python-${PYTHON_VERSION} && ./configure && \
    make && make install

# Pythonのインストールを確認
RUN python3 --version
WORKDIR /src