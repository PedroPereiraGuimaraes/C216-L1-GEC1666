import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)

API_NEWS_URL = os.getenv("API_NEWS_URL", 'http://localhost:5000/news')

@app.route('/')
def index():
    response = requests.get(f'{API_NEWS_URL}/all')
    news = response.json()
    return render_template('index.html', news=news)

@app.route('/edit', methods=['GET'])
def edit():
    response = requests.get(f'{API_NEWS_URL}/all')
    news = response.json()
    return render_template('news.html', news=news)

@app.route('/update/<string:id>', methods=['GET'])
def update(id):
    return render_template('update.html', news=id)

@app.route('/add', methods=['GET'])
def add():
    response = requests.get(f'{API_NEWS_URL}/all')
    news = response.json()
    return render_template('add.html', news=news)

@app.route('/add', methods=['POST'])
def add_news():
    title = request.form['title']
    content = request.form['content']
    payload = {
        'id': "",
        'title': title,
        'content': content,
    }
    response = requests.post(f'{API_NEWS_URL}/create', json=payload)
    
    if response.status_code == 200:
        return redirect(url_for('index'))
    else:
        return "Erro ao inserir noticia", 500
    
@app.route('/update/<string:id>', methods=['POST'])
def update_news(id):
    title = request.form['title']
    content = request.form['content']
    payload = {
        'id': id,
        'title': title,
        'content': content,
    }
    response = requests.post(f'{API_NEWS_URL}/update', json=payload)
    
    if response.status_code == 200:
        return redirect(url_for('index'))
    else:
        return "Erro ao inserir noticia", 500
    
@app.route('/delete/<string:id>', methods=['POST'])
def delete_news(id):
    response = requests.post(f'{API_NEWS_URL}/delete/{id}')
    
    if response.status_code == 200:
        return redirect(url_for('index'))
    else:
        return "Erro ao deletar notícia", 500

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')