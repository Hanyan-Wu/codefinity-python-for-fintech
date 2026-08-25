from sklearn.ensemble import IsolationForest

def detect_fraudulent_transactions(transactions):
    # Write your code here
    transactions = [[amt] for amt in transactions]
    iso_forest = IsolationForest(contamination="auto", random_state=42)

    iso_forest.fit(transactions)

    predict = iso_forest.predict(transactions)

    num_anomalies = len(predict[predict == -1])
    anomaly_indices = [i for i in range(len(predict)) if predict[i] == -1]
    # After determining the number of anomalies, print it as required
    
    # If all points are flagged as anomalies, treat as zero anomalies (edge case for uniform data)
    if num_anomalies == len(predict):
        print(0)  # <-- Print 0 here if no anomalies are detected
        return []
    else:    
        print(num_anomalies)  # <-- Print number of anomalies detected here after counting them
        return anomaly_indices

transactions = [50, 52, 48, 51, 49, 500, 53, 47, 2000, 54, 50, 48, 52, 49]
anomalies = detect_fraudulent_transactions(transactions)
print(anomalies)
# Remember: print(num_anomalies) somewhere in your function after you count them
