from sklearn.cluster import KMeans
import numpy as np

def cluster_asset_returns(asset_returns):
    asset_names = list(asset_returns.keys())
    returns_matrix = np.array([asset_returns[asset] for asset in asset_names])
    returns_matrix = returns_matrix.reshape(len(asset_names), -1)
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    kmeans.fit(returns_matrix)
    cluster_labels = kmeans.labels_
    asset_cluster_map = {asset_names[i]: int(cluster_labels[i]) for i in range(len(asset_names))}
    return asset_cluster_map

# Sample asset returns for demonstration
asset_returns = {
    "AAPL": [0.01, 0.02, -0.01, 0.03],
    "GOOG": [0.015, 0.025, -0.005, 0.027],
    "TSLA": [-0.02, -0.03, 0.01, -0.025],
    "JPM": [0.005, 0.007, 0.002, 0.008],
}

result = cluster_asset_returns(asset_returns)
print(result)
