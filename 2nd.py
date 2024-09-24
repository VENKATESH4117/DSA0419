import numpy as np
sales_data = np.array([[120, 155, 150], 
                       [85, 90, 95],  
                       [60, 75, 70]])
average_price = np.mean(sales_data)
print("Average price of products sold in the past month:", average_price)
