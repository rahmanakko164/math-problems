def find_max_profit(prices):
    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    
    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(find_max_profit(prices)) # Output: 9
