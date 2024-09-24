import pandas as pd
data = {
    'property_id': [1, 2, 3],
    'location': ['New York', 'San Francisco',  'Chicago'],
    'bedrooms': [3, 4, 5],
    'area': [1500, 2000, 2500],
    'listing_price': [500000, 750000, 1000000]
}
property_data = pd.DataFrame(data)
avg_listing_price_per_location = property_data.groupby('location')['listing_price'].mean()
print("Average listing price per location:")
print(avg_listing_price_per_location)
properties_more_than_4_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]
print(f"\nNumber of properties with more than 4 bedrooms: {properties_more_than_4_bedrooms}")
largest_property = property_data.loc[property_data['area'].idxmax()]
print("\nProperty with the largest area:")
print(largest_property)
