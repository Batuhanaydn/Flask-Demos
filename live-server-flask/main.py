from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/html/index.html')
app.run('127.0.0.1', 8090, debug=True)
