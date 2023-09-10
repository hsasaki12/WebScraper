# 基本となるイメージを指定
FROM python:3.9

# アプリケーションディレクトリを作成
WORKDIR /usr/src/app

# 必要なパッケージをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# すべてのローカルファイルをコピー
COPY . .

# Flaskが使用するポートを指定
EXPOSE 5000

# コマンド実行
CMD ["flask", "run", "--host=0.0.0.0"]
