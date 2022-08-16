import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(90), nullable=False)
    productStock = db.Column(db.Integer, nullable=False)
    productStore = db.Column(db.String(90), nullable=False)
    productCredit = db.Column(db.String(300), nullable=False)
    productDiscount = db.Column(db.Integer, nullable=False)
    productCode = db.Column(db.String(21), nullable=False)
    productPrice = db.Column(db.Integer, nullable=False)
    productPercent = db.Column(db.Integer, nullable=False)
    productActive = db.Column(db.Boolean, nullable=False)
    productCategory = db.Column(db.String(30), nullable=False)
    productRate = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Stock {self.productName} {(self.productPrice / (self.productDiscount * 100)) - self.productPrice}'


@app.route('/')
def main_page():
    stock = Stock.query.all()
    return render_template('index.html', stock=stock)

@app.route('/all')
def all_product_list():
    all_product = Stock.query.all()
    return render_template('all_product.html', all_product=all_product)

@app.route('/split-pages')
def split_pages():
    page = request.args.get('page', 1, type=int)
    pagination = Stock.query.order_by(Stock.productName).paginate(page, per_page=3)
    return render_template('split_pages.html', pagination=pagination)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)