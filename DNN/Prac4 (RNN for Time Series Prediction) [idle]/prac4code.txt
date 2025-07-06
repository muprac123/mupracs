import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Create synthetic time series data
def create_time_series_data():
    time = np.arange(0, 100, 0.1)
    series = np.sin(time) + np.random.normal(0, 0.1, len(time))
    series = series + time / 50
    return time, series

# Create input-output windows
def create_dataset(data, time_steps=10):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:(i + time_steps)])
        y.append(data[i + time_steps])
    return np.array(X), np.array(y)

# Generate time series
time, series = create_time_series_data()

# Scale data
scaler = MinMaxScaler(feature_range=(0, 1))
series_scaled = scaler.fit_transform(series.reshape(-1, 1))

# Prepare dataset
time_steps = 20
X, y = create_dataset(series_scaled, time_steps)
X = X.reshape(X.shape[0], X.shape[1], 1)

# Split into train and test
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Define model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(time_steps, 1)),
    tf.keras.layers.SimpleRNN(50, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile
model.compile(optimizer='adam', loss='mse')
model.summary()

# Train
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# Plot loss
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()

# Predict
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Inverse transform
train_predict = scaler.inverse_transform(train_predict)
y_train_inv = scaler.inverse_transform(y_train.reshape(-1, 1))
test_predict = scaler.inverse_transform(test_predict)
y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1))

# Calculate RMSE
train_rmse = np.sqrt(np.mean((train_predict - y_train_inv) ** 2))
test_rmse = np.sqrt(np.mean((test_predict - y_test_inv) ** 2))
print(f'Train RMSE: {train_rmse:.4f}')
print(f'Test RMSE: {test_rmse:.4f}')

# Plot predictions
plt.figure(figsize=(12, 6))
plt.plot(time, series, label='Original Series', alpha=0.5)

train_idx = np.arange(time_steps, time_steps + len(train_predict))
test_idx = np.arange(time_steps + len(train_predict), time_steps + len(train_predict) + len(test_predict))

plt.plot(time[train_idx], train_predict, 'b', label='Training Predictions')
plt.plot(time[test_idx], test_predict, 'r', label='Test Predictions')

plt.title('RNN Time Series Prediction')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid()
plt.show()

# Predict future
def predict_sequence(model, first_batch, n_steps):
    curr_batch = first_batch.copy()
    predicted = []

    for _ in range(n_steps):
        curr_pred = model.predict(curr_batch, verbose=0)[0][0]
        predicted.append(curr_pred)
        curr_batch = np.roll(curr_batch, -1, axis=1)
        curr_batch[0, -1, 0] = curr_pred

    return np.array(predicted)

future_steps = 100
last_batch = X_test[-1].reshape(1, time_steps, 1)
future_predictions = predict_sequence(model, last_batch, future_steps)
future_predictions = scaler.inverse_transform(future_predictions.reshape(-1, 1))

future_time = np.arange(time[-1], time[-1] + future_steps * 0.1, 0.1)

# Plot future predictions
plt.figure(figsize=(14, 6))
plt.plot(time, series, label='Original Series', alpha=0.5)
plt.plot(time[test_idx], test_predict, 'r', label='Test Predictions')
plt.plot(future_time, future_predictions, 'g', label='Future Predictions')
plt.axvline(x=time[-1], color='k', linestyle='--')
plt.title('RNN Time Series Prediction with Future Forecast')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid()
plt.show()
