import matplotlib.pyplot as plt

def plot_moving_average(prices, window):
    if window < 1 or window > len(prices):
        raise ValueError("Window size must be between 1 and the length of prices.")
    # sma = []
    sma = [None] * (window - 1)
    
    for i in range(window - 1, len(prices)):
        avg = sum(prices[i-window+1:i+1]) / window
        sma.append(avg)
        
    plt.figure(figsize=(10,5))
    plt.plot(prices, label="Price")
    plt.plot(sma, label=f"{window}-Day SMA")
    plt.xlabel("Day")
    plt.ylabel("Price")
    plt.title("Price and Simple Moving Average")
    plt.legend()
    plt.show()

prices = [100, 102, 101, 105, 110, 108, 112, 115, 117, 120]
window = 3
try:
    plot_moving_average(prices, window)
except ValueError as e:
    error_message = str(e)
    print(error_message)
