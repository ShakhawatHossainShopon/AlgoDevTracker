import numpy as np

prices = np.array([100.0, 102.5, 101.0, 104.0, 106.5])

simple_returns = (prices[1:] - prices[:-1]) / prices[:-1]
log_returns = np.diff(np.log(prices))

print("Close Prices:", prices)
print("Simple Returns (%):", np.round(simple_returns * 100, 2))
print("Log Returns (%):", np.round(log_returns * 100, 2))
print("Sum of Log Returns:", round(np.sum(log_returns), 4))
print("Total Period Log Return:", round(np.log(prices[-1] / prices[0]), 4))

X = np.array([
    [ 2.5, 1.8],
    [-1.5, 0.9],
    [ 3.0, 2.2],
    [ 2.4, 1.5]
])

mean = np.mean(X, axis=0)
std = np.std(X, axis=0)
X_scaled = (X - mean) / std

print("-" * 50)
print("Raw Trading Features (Momentum %, Volume Ratio):\n", X)
print("Feature Means (axis=0):", np.round(mean, 2))
print("Feature Standard Deviations (axis=0):", np.round(std, 2))
print("Scaled Features (Z-Score Standardized):\n", np.round(X_scaled, 2))
print("Scaled Features Mean (Should be ~0):", np.round(np.mean(X_scaled, axis=0), 2))
print("Scaled Features Std (Should be 1.0):", np.round(np.std(X_scaled, axis=0), 2))
