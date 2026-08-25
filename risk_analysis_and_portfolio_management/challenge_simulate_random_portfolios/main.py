import numpy as np

def simulate_random_portfolios():
    asset_returns = [0.08, 0.12, 0.15]
    portfolios = []
    
    for _ in range(100):
        weights = np.random.random(3)
        weights /= np.sum(weights)
        
        expected_return = np.dot(weights, asset_returns)
        std_dev = np.sqrt(np.dot(weights ** 2, [0.10 ** 2, 0.15 ** 2, 0.20 ** 2]))
        portfolio = {
            "weights": weights.tolist(),
            "expected_return": expected_return,
            "std_dev": std_dev
        }
        portfolios.append(portfolio)
    result = portfolios
    print(result)
    return portfolios

simulate_random_portfolios()
