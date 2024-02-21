import tkinter as tk

class ShoppingCartScreen(tk.Frame):
    def __init__(self, master, switch_screen):
        super().__init__(master)
        self.pack()
        self.create_widgets(switch_screen)

    def create_widgets(self, switch_screen):
        # Title
        title_label = tk.Label(self, text="Shopping Cart", font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=10)

        # Product list
        product_frame = tk.Frame(self)
        product_frame.pack(pady=10)

        # Example products in the cart
        products_in_cart = [
            {"name": "Product 1", "price": "$10.99", "quantity": 2},
            {"name": "Product 2", "price": "$24.99", "quantity": 1},
            # Add more products as needed
        ]

        for product in products_in_cart:
            self.create_product_entry(product_frame, product)

        # Recommended products
        recommended_frame = tk.Frame(self)
        recommended_frame.pack(side=tk.RIGHT, padx=10)

        # Example recommended products
        recommended_products = [
            {"name": "Recommended 1", "price": "$15.99"},
            {"name": "Recommended 2", "price": "$19.99"},
            # Add more recommended products as needed
        ]

        for recommended_product in recommended_products:
            self.create_recommended_entry(recommended_frame, recommended_product)

        # Total display
        total_label = tk.Label(self, text="Total: $35.97", font=('Helvetica', 12))
        total_label.pack(pady=10)

        # Buttons
        switch_button = tk.Button(self, text="Go to Recommended", command=lambda: switch_screen(RecommendedScreen))
        switch_button.pack(pady=10)

    def create_product_entry(self, frame, product):
        entry_label = tk.Label(frame, text=f"{product['name']} - {product['price']} - Quantity: {product['quantity']}")
        entry_label.pack()

        # Add to cart button
        add_button = tk.Button(frame, text="Add to Cart", command=lambda: self.add_to_cart(product))
        add_button.pack()

        # Remove button
        remove_button = tk.Button(frame, text="Remove", command=lambda: self.remove_from_cart(product))
        remove_button.pack()

        # Quantity field
        quantity_entry = tk.Entry(frame, width=5)
        quantity_entry.insert(0, str(product['quantity']))
        quantity_entry.pack()

    def create_recommended_entry(self, frame, recommended_product):
        entry_label = tk.Label(frame, text=f"{recommended_product['name']} - {recommended_product['price']}")
        entry_label.pack()

        # Add to cart button
        add_button = tk.Button(frame, text="Add to Cart", command=lambda: self.add_to_cart(recommended_product))
        add_button.pack()

    def add_to_cart(self, product):
        # Add your logic to update the cart with the selected product
        print(f"Added {product['name']} to the cart")

    def remove_from_cart(self, product):
        # Add your logic to remove the selected product from the cart
        print(f"Removed {product['name']} from the cart")

class RecommendedScreen(tk.Frame):
    def __init__(self, master, switch_screen):
        super().__init__(master)
        self.pack()
        self.create_widgets(switch_screen)

    def create_widgets(self, switch_screen):
        title_label = tk.Label(self, text="Recommended Products", font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=10)

        # Example recommended products
        recommended_products = [

        ]

        for recommended_product in recommended_products:
            self.create_recommended_entry(recommended_product)

        # Back button
        back_button = tk.Button(self, text="Go to Cart", command=lambda: switch_screen(ShoppingCartScreen))
        back_button.pack(pady=10)

    def create_recommended_entry(self, recommended_product):
        entry_label = tk.Label(self, text=f"{recommended_product['name']} - {recommended_product['price']}")
        entry_label.pack()

        # Add to cart button
        add_button = tk.Button(self, text="Add to Cart", command=lambda: print(f"Added {recommended_product['name']} to the cart"))
        add_button.pack()
v