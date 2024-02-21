import tkinter as tk
from tkinter import ttk
from data_preprocessing import *


class ProductListingScreen(tk.Frame):
    MORE_ITEMS = 20

    def __init__(self, master):
        super().__init__(master)
        self.click_count = 0
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self, text="Products", font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=10)

        # Search Bar
        search_bar = tk.Entry(self, width=30)
        search_bar.pack(pady=5)

        # Filters
        filters_frame = tk.Frame(self)
        filters_frame.pack(pady=10)

        category_label = tk.Label(filters_frame, text="Category:")
        category_label.grid(row=0, column=0, padx=5)

        category_options = ["All", "Electronics", "Clothing", "Home & Kitchen"]
        category_var = tk.StringVar()
        category_var.set("All")
        category_menu = tk.OptionMenu(filters_frame, category_var, *category_options)
        category_menu.grid(row=0, column=1, padx=5)

        price_label = tk.Label(filters_frame, text="Price Range:")
        price_label.grid(row=0, column=2, padx=5)

        price_options = ["All", "$0 - $50", "$50 - $100", "$100 and above"]
        price_var = tk.StringVar()
        price_var.set("All")
        price_menu = tk.OptionMenu(filters_frame, price_var, *price_options)
        price_menu.grid(row=0, column=3, padx=5)

        # Scrollable Product List
        product_canvas = tk.Canvas(self)
        product_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=product_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        product_canvas.configure(yscrollcommand=scrollbar.set)

        product_frame = tk.Frame(product_canvas)
        product_canvas.create_window((0, 0), window=product_frame, anchor=tk.NW)
        products_df = filereader('Data/processed_data/product_List.xlsx')

        self.display_product(product_canvas, product_frame, products_df, 0, 20)
        show_more_button = tk.Button(self, text="Show More",
                                     command=self.show_more_items(product_canvas, product_frame, products_df))
        show_more_button.pack(pady=10)

    def show_more_items(self, product_canvas, product_frame, products_df):
        # Calculate the next start index
        start = self.click_count * self.MORE_ITEMS
        end = start + self.MORE_ITEMS

        # Increment the click count
        self.click_count += 1
        print(end)
        # Display the next range of items
        self.display_product(product_canvas, product_frame, products_df, start, 30)

        # Update the product_canvas
        product_frame.update_idletasks()
        product_canvas.config(scrollregion=product_canvas.bbox("all"))

    def display_product(self, product_canvas, product_frame, products_df, start, end):
        # Clear existing widgets in product_frame
        for widget in product_frame.winfo_children():
            widget.destroy()

        # Display new set of items
        for _, product in products_df.iloc[start:end - 1].iterrows():
            product_dict = {
                "Name": product['Itemname'],
                "Price": f"${product['Price']:.2f}",
            }
            self.create_product_entry(product_frame, product_dict)

        # Update the product_canvas
        product_frame.update_idletasks()
        product_canvas.config(scrollregion=product_canvas.bbox("all"))
        print("more to display")

    def create_product_entry(self, frame, product):
        entry_frame = tk.Frame(frame, relief=tk.GROOVE, borderwidth=2)
        entry_frame.pack(pady=10, padx=10, side=tk.TOP, fill=tk.X)

        # Product Information
        name_label = tk.Label(entry_frame, text=product['Name'], font=('Helvetica', 12, 'bold'))
        name_label.grid(row=0, column=0, sticky=tk.W)

        price_label = tk.Label(entry_frame, text=product['Price'], font=('Helvetica', 10))
        price_label.grid(row=1, column=0, sticky=tk.W)

        # Purchase Options and Buttons
        options_frame = tk.Frame(entry_frame)
        options_frame.grid(row=0, column=1, sticky=tk.E)

        add_to_cart_button = tk.Button(options_frame, text="Add to Cart", command=lambda: self.add_to_cart(product))
        add_to_cart_button.grid(row=0, column=0, padx=5)

        view_more_button = tk.Button(options_frame, text="View More", command=lambda: self.view_more(product))
        view_more_button.grid(row=0, column=1, padx=5)

    def add_to_cart(self, product):
        # Assuming "Name" is the correct key for the product name
        print(f"Added {product['Name']} to the cart")

    def view_more(self, product):
        # Assuming "Name" is the correct key for the product name
        print(f"View more details about {product['Name']}")
