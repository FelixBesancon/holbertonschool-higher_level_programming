from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os


def create_database():
    if os.path.exists('products.db'):
        return

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    conn.commit()
    conn.close()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
        items = data.get('items', [])
    return render_template('items.html', items=items)

def read_json():
    with open('products.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        if isinstance(data, list):
            return data
        return data.get('products', [])

def read_csv():
    with open('products.csv', 'r', newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]
    except sqlite3.Error:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')

    products_list = []
    filtered_products = []
    error = None

    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    elif source == 'sql':
        products_list = read_sql()
    else:
        error = "Wrong source"
        return render_template('product_display.html', products=filtered_products, error=error)

    if not products_list:
        error = "Product not found"
        return render_template('product_display.html', products=filtered_products, error=error)

    product_id = request.args.get('id')

    if product_id is not None:
        for product in products_list:
            if str(product.get("id")) == str(product_id):
                filtered_products.append(product)
    else:
        filtered_products = products_list

    if not filtered_products:
        error = "Product not found"
        return render_template('product_display.html', products=filtered_products, error=error)

    return render_template('product_display.html', products=filtered_products, error=error)

if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
