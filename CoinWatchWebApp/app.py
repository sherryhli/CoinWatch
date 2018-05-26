from flask import Flask, render_template, flash, request
import json
import os
os.chdir('C:\\Users\\sherr\\source\\repos\\CoinWatch\\CoinWatchWebApp\\static')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        name = request.form.get("coinname".lower())
        with open('data.json') as d:
            data = json.loads(d.read())
        return render_template('result.html', result = data, name = name)
    
if __name__ == '__main__':
    app.run('localhost', 4449)

