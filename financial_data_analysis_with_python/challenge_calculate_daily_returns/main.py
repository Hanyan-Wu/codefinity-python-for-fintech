def calculate_daily_returns(prices):
    # Write your code here
    returns = [] 
    for i in range(1, len(prices)):
        daily_return = round(100*(prices[i] / prices[i-1] - 1), 4)
        returns.append(daily_return)
    return returns

prices = [100, 102, 101]
result = calculate_daily_returns(prices)
print(result)
