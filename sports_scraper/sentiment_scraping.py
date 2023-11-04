from flask import Flask, jsonify
import requests
import pandas as pd

app = Flask(__name__)

df_descriptions = pd.DataFrame(columns=['description'])

@app.route('/', methods=['GET'])
def init():
    return "hello nfl user"

@app.route('/fetch-nfl-news', methods=['GET'])
def fetch_nfl_news():
    global df_descriptions
    response = requests.get('http://site.api.espn.com/apis/site/v2/sports/football/nfl/news')

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

        descriptions = [{'description': article.get('description', '')} for article in articles]
        df_descriptions = pd.DataFrame(descriptions)
        
        df_descriptions.to_csv('nfl_news_descriptions.csv', index=False)
        
        return jsonify({
            "status": "success",
            "message": "Retrieved current news descriptions",
            "data": df_descriptions.to_dict(orient='records')
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Failed to fetch news data"
        }), response.status_code

if __name__ == '__main__':
    app.run(debug=True)