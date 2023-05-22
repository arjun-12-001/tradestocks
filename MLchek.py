import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
import database as db

def model_run(company):
    # download stock data
    stock = yf.download(company, period="18mo")

    # create a new dataframe with only the 'Close' column
    data = stock.filter(['Close'])

    # convert the dataframe to a numpy array
    dataset = data.values

    # scale the data
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(dataset)

    # split the data into training and testing sets
    train_data = scaled_data[:-20, :]
    test_data = scaled_data[-20:, :]

    # split the training data into x_train and y_train datasets
    x_train = []
    y_train = []
    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i, 0])
        y_train.append(train_data[i, 0])

    # convert the x_train and y_train datasets to numpy arrays
    x_train, y_train = np.array(x_train), np.array(y_train)

    # reshape the data for the LSTM model
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # build the LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))

    # compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # train the model
    model.fit(x_train, y_train, epochs=30, batch_size=32)

    # predict the future stock prices
    inputs = data[-80:].values
    inputs = scaler.transform(inputs)
    x_future = []
    for i in range(60, 80):
        x_future.append(inputs[i-60:i, 0])
    x_future = np.array(x_future)
    x_future = np.reshape(x_future, (x_future.shape[0], x_future.shape[1], 1))
    predicted_prices = model.predict(x_future)
    predicted_prices = scaler.inverse_transform(predicted_prices)

    # create a dataframe to store the predicted prices
    dates = pd.date_range(start=data.index[-1], periods=20, freq='B')
    future_prices = pd.DataFrame(data=predicted_prices, index=dates, columns=['Close'])

    val = data.Close[-1]-future_prices.Close[0]
    future_prices.Close = future_prices.Close + val
    # db.lstm_data(future_prices,company)

    return data,future_prices

    # import matplotlib.pyplot as plt
    # plt.figure(figsize=(16, 8))
    # plt.title('LSTM Model')
    # plt.xlabel('Date', fontsize=18)
    # plt.ylabel('Close Price USD ($)', fontsize=18)
    # plt.plot(data['Close'])
    # plt.plot(future_prices['Close'])
    # plt.legend(['Historical Prices', 'Predicted Prices'], loc='lower right')
    # plt.show()

#------------------------------------------------------------#