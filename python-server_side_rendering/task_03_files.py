from flask import Flask, render_template, request
import json
import csv

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
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    with open('products.csv', 'r', newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

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
    else:
        error = "Wrong source"
        return render_template('product_display.html', products=filtered_products, error=error)

    if not products_list:
        error = "Product not found"
        return render_template('product_display.html', products=filtered_products, error=error)

    product_id = request.args.get('id')

    if product_id is not None:
        for product in products_list:
            if str(product["id"]) == str(product_id):
                filtered_products.append(product)
    else:
        filtered_products = products_list

    if not filtered_products:
        error = "Product not found"
        return render_template('product_display.html', products=filtered_products, error=error)

    return render_template('product_display.html', products=filtered_products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
