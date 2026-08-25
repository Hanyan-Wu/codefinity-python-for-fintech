import numpy as np

def analyze_sharpe_ratio(returns, risk_free_rate):
    # Write your code here
    message = ""

    avg = np.mean(returns)
    std = np.std(returns, ddof=0)

    sharpe = (avg - risk_free_rate) / std if std != 0 else 0

    if sharpe > 1:
        message += 'good'
    elif sharpe > 0:
        message += 'average'
    else:
        message += 'poor'
        
    print(message)

    return sharpe

returns = [0.05, 0.02, 0.04, -0.01, 0.03]
risk_free_rate = 0.01
result = analyze_sharpe_ratio(returns, risk_free_rate)
