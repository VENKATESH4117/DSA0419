import pandas as pd
data = {
    'customer_id': [101, 102, 101, 103],
    'order_date': ['2023-01-15', '2023-02-20', '2023-01-22', '2023-03-10'],
    'product_name': ['A', 'B', 'A', 'C'],
    'order_quantity': [2, 1, 3, 4]
}
order_data = pd.DataFrame(data)
order_data['order_date'] = pd.to_datetime(order_data['order_date'])
print(order_data.groupby('customer_id').size())
print(order_data.groupby('product_name')['order_quantity'].mean())
print(order_data['order_date'].min())
print(order_data['order_date'].max())
