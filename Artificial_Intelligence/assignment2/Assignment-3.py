import numpy as np
import tensorflow as tf
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.optimizers import Adam

# CIFAR-10 데이터셋을 읽고 신경망에 입력할 형태로 변환
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train.astype(np.float32) / 255.0
x_test = x_test.astype(np.float32) / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# 신경망 모델 설계
cnn = Sequential()
cnn.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
cnn.add(Conv2D(32, (3, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Dropout(0.25))
cnn.add(Conv2D(64, (3, 3), activation='relu'))
cnn.add(Conv2D(64, (3, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Dropout(0.25))
cnn.add(Flatten())
cnn.add(Dense(128, activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(10, activation='softmax'))

# 신경망 모델 학습
cnn.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
hist = cnn.fit(x_train, y_train, batch_size=128, epochs=30, validation_data=(x_test, y_test), verbose=2)

# 신경망 모델 정확률 평가
res = cnn.evaluate(x_test, y_test, verbose=0)
print("1순위 정확률은", res[1] * 100)

# 다중 순위 정확률 계산
predictions = cnn.predict(x_test)
top1_accuracy = np.mean(np.argmax(predictions, axis=1) == np.argmax(y_test, axis=1)) * 100

# 5순위 정확률 계산
sorted_indices = np.argsort(predictions, axis=1)[:, ::-1]
top5_accuracy = np.mean(np.any(sorted_indices[:, :5] == np.argmax(y_test, axis=1).reshape((-1, 1)), axis=1)) * 100

print("1순위 정확률은", top1_accuracy)
print("5순위 정확률은", top5_accuracy)