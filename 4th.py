import numpy as np
sales_data = np.array([10000, 20000, 30000, 40000])
total_sales = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print("Total sales for the year:", total_sales)
print("Percentage increase in sales from Q1 to Q4:", percentage_increase)
