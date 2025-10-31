from flask import Flask,render_template,request,redirect,url_for,flash
from database import fetch_data,insert_products,insert_stocks,insert_sales,profit_per_product,sales_per_product

app=Flask(__name__)

app.secret_key="yourkey"

@app.route('/')
def home():
    return render_template('index.html')

# products route
@app.route('/products')
def products():
    products=fetch_data("products")
    return render_template('products.html', products = products)

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method== 'POST':
        productname = request.form["productname"]
        buyingprice = request.form["buyingprice"]
        sellingprice = request.form["sellingprice"]

        new_products = (productname,buyingprice,sellingprice)
        insert_products(new_products)
    
        flash("Product added successfully","success")
    return redirect(url_for('products'))


# Sales route 
@app.route('/sales')
def sales():
    sales=fetch_data("sales")
    products=fetch_data("products")
    return render_template('sales.html', sales = sales ,products = products)

@app.route('/make_sale', methods=['GET','POST'])
def make_sale():
    if request.method == 'POST':
        pid= request.form["pid"]
        quantity= request.form["quantity"]

        new_sale=(pid,quantity)
    
        insert_sales(new_sale)
        flash("Sale made successfully","success")
    return redirect(url_for('sales'))

# stocks route 
@app.route('/stocks')
def stocks():
    stocks=fetch_data("stocks")
    products=fetch_data("products")
    return render_template('stocks.html', stocks = stocks, products = products)

@app.route('/manage_stock',methods=['GET','POST'])
def manage_stock():
    if request.method== 'POST':
        pid = request.form["pid"]
        stockquantity= request.form["stockquantity"]

        new_stock=(pid,stockquantity)
        insert_stocks(new_stock)

        flash("Stock updated successfully","success")

    return redirect(url_for('stocks'))

@app.route('/dashboard')
def dashboard():
    product_profit = profit_per_product() 
    product_sales = sales_per_product()

    product_names = [i[0] for i in product_profit]
    profit_values = [float(i[1]) for i in product_profit]

    sales_names = [i[0] for i in product_sales]
    sales_values = [float(i[1]) for i in product_sales]
   


    return render_template("dashboard.html", product_names=product_names, profit_values=profit_values, sales_values=sales_values, sales_names=sales_names)



app.run(debug=True)