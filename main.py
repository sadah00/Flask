from flask import Flask,render_template
from database import fetch_data

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# products route
@app.route('/products')
def products():
    products=fetch_data("products")
    return render_template('products.html', products = products)

# Sales route 
@app.route('/sales')
def sales():
    sales=fetch_data("sales")
    return render_template('sales.html', sales = sales)

# stocks route 
@app.route('/stocks')
def stocks():
    stocks=fetch_data("stocks")
    return render_template('stocks.html', stocks = stocks)




app.run(debug=True)