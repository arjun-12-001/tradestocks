from keras.models import Sequential
from keras.layers import Dense, LSTM
import data_preprocess as dp

X_train,X_test,y_train,y_test = dp.preprocess()
#Creating LSTM model using keras
model = Sequential()
model.add(LSTM(units=50,return_sequences=True,input_shape=(X_train.shape[1],1)))
model.add(LSTM(units=50,return_sequences=True))
model.add(LSTM(units=50))
model.add(Dense(units=1,activation='linear'))
print(model.summary())
#Training model with adam optimizer and mean squared error loss function
model.compile(loss='mean_squared_error',optimizer='adam')
model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=20,batch_size=64)
#PLotting loss, it shows that loss has decreased significantly and model trained well
loss = model.history.history['loss']