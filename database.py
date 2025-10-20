import select
import psycopg2

conn = psycopg2.connect(host="localhost", port="5432", user="postgres", password="kimysada6",dbname="myduka_datab")
cur=conn.cursor()

def get_products():
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    return products

#print(get_products())
    
# displaying sales
def get_sales():
    cur.execute("SELECT * FROM sales")
    sales = cur.fetchall()
    return sales

def insert_sales(sale_values):
    cur.execute(f"INSERT INTO sales (pid, quantity) VALUES {sale_values}")
    conn.commit()


def get_stock():
    cur.execute("SELECT * FROM stock")
    stock = cur.fetchall()
    return stock