import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Normalization, Dropout
import matplotlib.pyplot as plt
df = pd.read_csv("thing.csv")
x = df.iloc[:,1:]
x1 = Normalization()
x1.adapt(x)
y = df["wp"]
X_train, X_test, y_train, y_test = train_test_split(x,y)
model = Sequential()
model.add(Dense(units=120, kernel_initializer='normal', activation='linear', input_dim=len(X_train.columns)))
model.add(Dropout(.4))
model.add(Dense(units=120, kernel_initializer='normal',activation='linear'))
model.add(Dense(units=1, kernel_initializer='normal',activation='relu'))
model.compile(loss='mean_absolute_error', optimizer='adam')
model.fit(X_train, y_train, epochs=200, batch_size=30, validation_split = 0.2)
y_hat = model.predict(X_test)
y_test = y_test.reset_index(drop = True)
y_test = y_test.to_frame()
y_test.insert(0, "prediction",y_hat)
plt.plot(y_test)
plt.show()