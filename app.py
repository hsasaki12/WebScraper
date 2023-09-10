from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url', default='https://www.example.com', type=str)

    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve the webpage.'}), 500
    
    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.title.string if soup.title else 'No title found'
    return render_template('index.html', title=title_tag)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
