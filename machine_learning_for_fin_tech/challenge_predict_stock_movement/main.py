import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def predict_stock_movement(prices):
    df = pd.DataFrame({'Close': prices})
    # Calculate previous day's return
    df['Prev_Return'] = df['Close'].pct_change()
    # Calculate 3-day moving average
    df['MA_3'] = df['Close'].rolling(window=3).mean()
    # Target: 1 if price goes up next day, 0 otherwise
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    # Drop any rows with NaN values resulting from feature calculations
    df = df.dropna()
    X = df[['Prev_Return', 'MA_3']]
    y = df['Target']
    # Split into training and test sets (80% train, 20% test), no shuffle
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    # Train logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    # Predict on test set
    y_pred = model.predict(X_test)
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

prices = [
    100.0, 101.5, 102.0, 101.0, 102.5, 103.0, 102.8,
    104.0, 105.5, 104.5, 106.0, 105.0, 106.5, 107.0
]
acc = predict_stock_movement(prices)
print(acc)