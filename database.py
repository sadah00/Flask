import select
import psycopg2

conn = psycopg2.connect(host="localhost", port="5432", user="postgres", password="kimysada6",dbname="myduka_datab")
cur=conn.cursor()


# FETCHING VALUES

def fetch_data(table_name):
    cur.execute(f"SELECT * FROM {table_name}")
    data=cur.fetchall()
    return data

# products=fetch_data("products")
# sales=fetch_data("sales")
# stocks=fetch_data("stocks")
# print(products)
# print(sales)
# print(stocks)

# def fetch_products():
#     cur.execute("SELECT * FROM products")
#     products = cur.fetchall()
#     return products

# def insert_products(product_values):
#     query = "INSERT INTO products (name,buyingprice,sellingprice) VALUES (%s, %s, %s)"
#     cur.execute(query, product_values)
#     conn.commit()

#print(fetch_products())
    
# def fetch_sales():
#     cur.execute("SELECT * FROM sales")
#     sales = cur.fetchall()
#     return sales

# def insert_sales(sale_values):
#     cur.execute(f"INSERT INTO sales (pid, quantity) VALUES {sale_values}")
#     conn.commit()


# def fetch_stock():
#     cur.execute("SELECT * FROM stock")
#     stock = cur.fetchall()
#     return stock

# def insert_stock(stock_values):
#     cur.execute(f"INSERT INTO stock (pid,stockquantity) VALUES{stock_values}")
#     conn.commit()


# INSERTING VALUES

def insert_products(values):
    query = "insert into products(name,buyingprice,sellingprice)values(%s,%s,%s);"
    cur.execute(query,values)
    conn.commit()

# new_product=('Avocados',50,70)
# insert_products(new_product)
# products = fetch_data('products')
# print(products)

def insert_sales(values):
    query='insert into sales(pid,quantity)values(%s,%s);'
    cur.execute(query,values)
    conn.commit()
    
# new_sale=(2,5)
# insert_sales(new_sale)
# sales = fetch_data('sales')
# print(sales)

def insert_stocks(values):
    query="insert into stocks(pid,stockquantity)values(%s,%s);"
    cur.execute(query,values)
    conn.commit()

new_stock=(1,12)
#insert_stock(new_stock)


def profit_per_product():
    cur.execute("""
    select products.name as p_name ,sum((products.sellingprice - products.buyingprice) * sales.quantity) as profit from
    sales join products on sales.pid = products.id group by(p_name);
    """)
    product_profit = cur.fetchall()
    return product_profit

# myprofits=profit_per_product()
# print(f'my products profit {myprofits}')

def sales_per_product():
    cur.execute("""
        select products.name as p_name, sum(sales.quantity * products.sellingprice) as tota_sales
        from products join sales on products.id = sales.pid group by(p_name);
    """)
    product_sales = cur.fetchall()
    return product_sales

# mysales=sales_per_product()
# print(f'my products sales {mysales}')

def sales_per_day():
    cur.execute("""
    select date(sales.createdat) as date, sum(products.sellingprice * sales.quantity) as
    total_sales from products inner join sales on sales.pid = products.id group by(date);
    """)
    daily_sales = cur.fetchall()
    return daily_sales

def profit_per_day():
    cur.execute("""
        select date(sales.createdat) as date, sum((products.sellingprice - products.buyingprice)* sales.quantity) as 
        profit from sales join products on products.id = sales.pid group by(date);
    """)
    daily_profit = cur.fetchall()
    return daily_profit


def insert_users(values):
    query="insert into users(full_name,email,password)values(%s,%s,%s);"
    cur.execute(query,values)
    conn.commit()