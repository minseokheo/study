import numpy as np
import tensorflow as tf
from keras.datasets import mnist

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# MNIST 읽어 와서 신경망에 입력할 형태로 변환
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 784)                       # 텐서 모양 변환
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype(np.float32)/255.0                  # ndarray로 변환
x_test = x_test.astype(np.float32)/255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)        # 원핫 코드로 변환
y_test = tf.keras.utils.to_categorical(y_test, 10)

n_input = 784
n_hidden1 = 1024
n_hidden2 = 512
n_hidden3 = 512
n_hidden4 = 512
n_output = 10

# glorot_uniform
mlp1 = Sequential()
mlp1.add(Dense(units=n_hidden1, activation='tanh', input_shape=(n_input,)))
mlp1.add(Dense(units=n_hidden2, activation='tanh'))
mlp1.add(Dense(units=n_hidden3, activation='tanh'))
mlp1.add(Dense(units=n_hidden4, activation='tanh'))
mlp1.add(Dense(units=n_output, activation='tanh'))

mlp1.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.001),metrics=['accuracy'])
hist1 = mlp1.fit(x_train, y_train, batch_size=128, epochs=30, validation_data=(x_test, y_test), verbose=2)

res1 = mlp1.evaluate(x_test, y_test, verbose=0)
print("정확률은",res1[1]*100)
import matplotlib.pyplot as plt

# 정확률 곡선
plt.plot(hist1.history['accuracy'])
plt.plot(hist1.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.grid()
plt.show()

# 손실 함수 곡선
plt.plot(hist1.history['loss'])
plt.plot(hist1.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.grid()
plt.show()


# glorot_normal
mlp2 = Sequential()
mlp2.add(Dense(units=n_hidden1, activation='tanh', input_shape=(n_input,), kernel_initializer='glorot_normal', bias_initializer='zeros'))
mlp2.add(Dense(units=n_hidden2, activation='tanh', kernel_initializer='glorot_normal', bias_initializer='zeros'))
mlp2.add(Dense(units=n_hidden3, activation='tanh', kernel_initializer='glorot_normal', bias_initializer='zeros'))
mlp2.add(Dense(units=n_hidden4, activation='tanh', kernel_initializer='glorot_normal', bias_initializer='zeros'))
mlp2.add(Dense(units=n_output, activation='tanh', kernel_initializer='glorot_normal', bias_initializer='zeros'))

mlp2.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.001),metrics=['accuracy'])
hist2 = mlp2.fit(x_train, y_train, batch_size=128, epochs=30, validation_data=(x_test, y_test), verbose=2)

res2 = mlp2.evaluate(x_test, y_test, verbose=0)
print("정확률은",res2[1]*100)
import matplotlib.pyplot as plt

# 정확률 곡선
plt.plot(hist2.history['accuracy'])
plt.plot(hist2.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.grid()
plt.show()

# 손실 함수 곡선
plt.plot(hist2.history['loss'])
plt.plot(hist2.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.grid()
plt.show()


# random_normal
mlp3 = Sequential()
mlp3.add(Dense(units=n_hidden1, activation='tanh', input_shape=(n_input,), kernel_initializer='random_normal', bias_initializer='zeros'))
mlp3.add(Dense(units=n_hidden2, activation='tanh', kernel_initializer='random_normal', bias_initializer='zeros'))
mlp3.add(Dense(units=n_hidden3, activation='tanh', kernel_initializer='random_normal', bias_initializer='zeros'))
mlp3.add(Dense(units=n_hidden4, activation='tanh', kernel_initializer='random_normal', bias_initializer='zeros'))
mlp3.add(Dense(units=n_output, activation='tanh', kernel_initializer='random_normal', bias_initializer='zeros'))

mlp3.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.001),metrics=['accuracy'])
hist3 = mlp3.fit(x_train, y_train, batch_size=128, epochs=30, validation_data=(x_test, y_test), verbose=2)

res3 = mlp3.evaluate(x_test, y_test, verbose=0)
print("정확률은",res3[1]*100)
import matplotlib.pyplot as plt

# 정확률 곡선
plt.plot(hist3.history['accuracy'])
plt.plot(hist3.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.grid()
plt.show()

# 손실 함수 곡선
plt.plot(hist3.history['loss'])
plt.plot(hist3.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.grid()
plt.show()