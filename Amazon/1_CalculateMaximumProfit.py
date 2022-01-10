def MaximumProfit(Stock_price):
    max_profit, current_val = 0, 0
    for price in reversed(Stock_price):
        current_val = max(current_val, price)
        potential_profit = current_val-price
        max_profit = max(potential_profit, max_profit)
    return max_profit


Stock_price = [10, 8, 7, 5, 15, 7]
print(MaximumProfit(Stock_price))
