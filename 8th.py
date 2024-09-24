import pandas as pd
data = {
    'product_name': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'D', 'E', 'B'],
    'quantity_sold': [20, 15, 30, 10, 25, 40, 50, 5, 8, 35]
}
sales_data = pd.DataFrame(data)
total_sales_per_product = sales_data.groupby('product_name')['quantity_sold'].sum()
top_5_products = total_sales_per_product.nlargest(5)
print("Top 5 products sold the most:")
print(top_5_products)
