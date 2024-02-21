import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from warnings import filterwarnings
import pandas as pd

filterwarnings("ignore")


def calculate_revenue(data):
    data['Revenue'] = data['Quantity'] * data['Price']


def top_products_by_revenue(data):
    top_products = data.groupby('Itemname')['Revenue'].sum().nlargest(10).reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Itemname', y='Revenue', data=top_products, palette='viridis')
    plt.title('Top 10 Products by Revenue')
    plt.xlabel('Product')
    plt.ylabel('Revenue (in K)')
    plt.xticks(rotation=45, ha='right')


def top_customers_by_revenue(data):
    top_customers = data.groupby('CustomerID')['Revenue'].sum().nlargest(10).reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x='CustomerID', y='Revenue', data=top_customers, palette='viridis')
    plt.title('Top 10 Customers by Revenue')
    plt.xlabel('CustomerID')
    plt.ylabel('Revenue (in K)')
    plt.xticks(rotation=45, ha='right')


def top_countries_by_revenue(data):
    top_countries = data.groupby('Country')['Revenue'].sum().nlargest(10).reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Country', y='Revenue', data=top_countries, palette='viridis')
    plt.title('Top 10 Countries by Revenue')
    plt.xlabel('Country')
    plt.ylabel('Revenue (in Million)')
    plt.xticks(rotation=45, ha='right')


def total_revenue_by_month_in_year(data):
    data['Date'] = pd.to_datetime(data['Date'])
    data['Month'] = data['Date'].dt.strftime('%m/%Y')  # Format month as MM/YYYY
    # Calculate total revenue by month
    monthly_revenue = data.groupby('Month')['Revenue'].sum().reset_index()
    # Plotting
    plt.figure(figsize=(20, 6))
    sns.barplot(x='Month', y='Revenue', data=monthly_revenue, palette='viridis')
    plt.title(f'Total Revenue by Month ')
    plt.xlabel('Month')
    plt.ylabel('Revenue (in K)')
    plt.xticks(rotation=45, ha='right')


def visualize_all(data):
    calculate_revenue(data)
    top_products_by_revenue(data)
    top_customers_by_revenue(data)
    top_countries_by_revenue(data)
    total_revenue_by_month_in_year(data)
    plt.show()

# Example usage
# Assuming your DataFrame is named 'data'
# Call the visualize_all function to show all visualizations
