from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            return f"Error: {e}"

        # BeautifulSoupで整形したHTMLを取得
        soup = BeautifulSoup(response.text, 'html.parser')
        pretty_html = soup.prettify()
        
        return render_template('index.html', pretty_html=pretty_html)
        
    return render_template('index.html', pretty_html=None)

if __name__ == '__main__':
    app.run(debug=True)
