## Flask Web Scraper
このプロジェクトは、指定されたウェブページのHTMLタイトルを取得する簡単なWebスクレイピングAPIを提供します。Flask, BeautifulSoup, と Requestsを使用しています。

### インストール
### Dockerを使用する場合
Dockerイメージをビルドします。

```
docker build -t my_flask_scraper .
```
コンテナを起動します。

```
docker run -p 5000:5000 my_flask_scraper
```
これでhttp://localhost:5000/scrape?url=[YOUR_URL]にアクセスしてAPIを使用できます。

ローカルで実行する場合
必要なPythonパッケージをインストールします。

```
pip install -r requirements.txt
```
アプリケーションを起動します。

### 注意事項
Webスクレイピングを行う際には、対象となるウェブサイトの利用規約を確認してください。
頻繁なスクレイピングはサーバーに負荷をかける可能性があります。適切な間隔やレート制限を設定してください。
