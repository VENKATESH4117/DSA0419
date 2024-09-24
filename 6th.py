def calculate_total_cost(item_prices, item_quantities, discount_rate, tax_rate):
    total_cost_before_discount = sum([price * quantity for price, quantity in zip(item_prices, item_quantities)])
    discount = (discount_rate / 100) * total_cost_before_discount
    total_cost_after_discount = total_cost_before_discount - discount
    tax = (tax_rate / 100) * total_cost_after_discount
    final_total_cost = total_cost_after_discount + tax
    print(f"Total cost after applying {discount_rate}% discount and {tax_rate}% tax: ${final_total_cost:.2f}")
    return final_total_cost
item_prices = [10.00, 15.00, 7.50, 20.00]
item_quantities = [2, 1, 4, 3]
discount_rate = 10
tax_rate = 5
calculate_total_cost(item_prices, item_quantities, discount_rate, tax_rate)
