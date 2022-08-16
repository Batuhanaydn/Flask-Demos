from flask import Flask, render_template, request, url_for, redirect, flash, get_flashed_messages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

messages = [{'title': 'Messages',
            'content': 'Messages Content'},
            {'title': 'Messages 2',
            'content': 'Messages Content'}]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)