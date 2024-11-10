def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0
    
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)

    return max_profit

# Taking input from the user
n = int(input("Enter the number of days: "))
prices = []
print("Enter the prices for each day:")
for _ in range(n):
    price = int(input())
    prices.append(price)

# Calculating the maximum profit
result = max_profit(prices)
print("Maximum profit:", result)
