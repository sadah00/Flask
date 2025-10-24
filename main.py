from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# products route
@app.route('/products')
def products():
    return render_template('products.html')

# Sales route 
@app.route('/sales')
def sales():
    return render_template('sales.html')

# stocks route 
@app.route('/stocks')
def stocks():
    return render_template('stocks.html')




app.run(debug=True)