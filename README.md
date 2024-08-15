## Flask Application Design for an Electronic Purchasing System

### HTML Files

- **index.html:** The main page that displays a list of products and allows users to add them to their cart.
- **product_page.html:** Provides detailed information about a specific product, including its description, price, and quantity available.
- **cart.html:** Displays the items in the user's cart, allowing them to checkout or continue shopping.
- **checkout.html:** Collects user information and payment details for order processing.

### Routes

- **@app.route('/')** ("/" route): Displays the home page (index.html) with the list of products.
- **@app.route('/product_page/<product_id>')** ("/product_page/<product_id>" route): Renders the product page for a specific product, based on the `product_id` (e.g., "/product_page/123").
- **@app.route('/add_to_cart/<product_id>')** ("/add_to_cart/<product_id>" route): Adds the product with the given `product_id` to the user's cart and redirects to the product page.
- **@app.route('/cart')** ("/cart" route): Displays the cart page (cart.html) containing the user's selected products.
- **@app.route('/checkout')** ("/checkout" route): Renders the checkout page (checkout.html) for user information and payment processing.
- **@app.route('/process_order')** ("/process_order" route): Receives and processes the checkout form data, confirms the order, and directs the user to the order confirmation page.