
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# In-memory database for products
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.0, 'quantity': 10},
    {'id': 2, 'name': 'Product 2', 'price': 15.0, 'quantity': 15},
    {'id': 3, 'name': 'Product 3', 'price': 20.0, 'quantity': 20},
]

# In-memory cart
cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product_page/<int:product_id>')
def product_page(product_id):
    product = [product for product in products if product['id'] == product_id][0]
    return render_template('product_page.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = [product for product in products if product['id'] == product_id][0]
    cart.append(product)
    return redirect(url_for('product_page', product_id=product_id))

@app.route('/cart')
def cart_page():
    return render_template('cart.html', cart=cart)

@app.route('/checkout')
def checkout_page():
    return render_template('checkout.html')

@app.route('/process_order', methods=['POST'])
def process_order():
    # Process checkout form data and confirm order...
    return render_template('order_confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
