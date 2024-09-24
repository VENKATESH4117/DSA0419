import numpy as np
house_data = np.array([[3, 1500, 300000],  
                       [5, 2000, 450000],
                       [4, 1800, 350000],
                       [6, 2500, 600000]])
filtered_houses = house_data[house_data[:, 0] > 4]
average_sale_price = np.mean(filtered_houses[:, 2]) if filtered_houses.size > 0 else 0

print("Average sale price of houses with more than four bedrooms:", average_sale_price)
