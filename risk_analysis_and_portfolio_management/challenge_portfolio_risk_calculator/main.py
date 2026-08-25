import numpy as np

def portfolio_metrics(asset1_returns, asset2_returns, weight1, weight2):
    # Write your code here
    if weight1 + weight2 != 1:
        raise ValueError('Weights should sum to 1.')
    
    returns = np.array([asset1_returns, asset2_returns])
    weights = np.array([weight1, weight2])
    
    returns_p = np.dot(weights, returns)
    mean_p = np.mean(returns_p)
    sd_p = np.std(returns_p, ddof=1)
    # roh_p = np.corrcoef(asset1_returns, asset2_returns)
    # sd_1 = np.std(asset1_returns)
    # sd_2 = np.std(asset2_returns)
    # cov_p = (
    #     sd_1**2 * weight1**2 
    #     + sd_2**2 * weight2**2
    #     + 2 * roh_p * sd_1 * sd_2
    # )

    return (mean_p, sd_p)

returns_a = [0.01, 0.02, 0.015, 0.03, 0.005]
returns_b = [0.012, 0.018, 0.017, 0.025, 0.009]

result = portfolio_metrics(returns_a, returns_b, 0.6, 0.4)
print(result)

try:
    result_invalid = portfolio_metrics(returns_a, returns_b, 0.7, 0.4)
    print(result_invalid)
except ValueError as e:
    error_message = str(e)
    print(error_message)
