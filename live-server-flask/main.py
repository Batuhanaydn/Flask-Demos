# pip install flask-liveserver

from flask import Flask
from liveserver import LiveServer

app = Flask(__name__)

ls = LiveServer(app)

@app.route('/')
def index():
    return ls.render_template('index.html')
ls.run('127.0.0.1', 8081)