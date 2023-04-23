from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np

# MNIST 데이터셋을 읽고 훈련 집합과 테스트 집합으로 분할
mnist=fetch_openml('mnist_784')
mnist.data=mnist.data/255.0
x_train=mnist.data[:60000]; x_test=mnist.data[60000:]
y_train=np.int16(mnist.target[:60000]); y_test=np.int16(mnist.target[60000:])

################
# 본인 코드 작성
################

# 은닉층 1개
mlp1=MLPClassifier(hidden_layer_sizes=(100),learning_rate_init=0.001,batch_size=512,max_iter=300,solver='adam',verbose=False)
mlp1.fit(x_train,y_train)

res1=mlp1.predict(x_test)

no_correct1=sum(res1 == y_test)
accuracy1=no_correct1/len(res1)
print("(은닉층 1개)테스트 집합에 대한 정확률은", accuracy1*100, "%입니다.")


# 은닉층 2개
mlp2=MLPClassifier(hidden_layer_sizes=(100, 100),learning_rate_init=0.001,batch_size=512,max_iter=300,solver='adam',verbose=False)
mlp2.fit(x_train,y_train)

res2=mlp2.predict(x_test)

no_correct2=sum(res2 == y_test)
accuracy2=no_correct2/len(res2)
print("(은닉층 2개)테스트 집합에 대한 정확률은", accuracy2*100, "%입니다.")


# 은닉층 3개
mlp3=MLPClassifier(hidden_layer_sizes=(100, 100, 100),learning_rate_init=0.001,batch_size=512,max_iter=300,solver='adam',verbose=False)
mlp3.fit(x_train,y_train)

res3=mlp3.predict(x_test)

no_correct3=sum(res3 == y_test)
accuracy3=no_correct3/len(res3)
print("(은닉층 3개)테스트 집합에 대한 정확률은", accuracy3*100, "%입니다.")


# 은닉층 4개
mlp4=MLPClassifier(hidden_layer_sizes=(100, 100, 100, 100),learning_rate_init=0.001,batch_size=512,max_iter=300,solver='adam',verbose=False)
mlp4.fit(x_train,y_train)

res4=mlp4.predict(x_test)

no_correct4=sum(res4 == y_test)
accuracy4=no_correct4/len(res4)
print("(은닉층 4개)테스트 집합에 대한 정확률은", accuracy4*100, "%입니다.")


# 은닉층 5개
mlp5=MLPClassifier(hidden_layer_sizes=(100, 100, 100, 100, 100),learning_rate_init=0.001,batch_size=512,max_iter=300,solver='adam',verbose=False)
mlp5.fit(x_train,y_train)

res5=mlp5.predict(x_test)

no_correct5=sum(res5 == y_test)
accuracy5=no_correct5/len(res5)
print("(은닉층 5개)테스트 집합에 대한 정확률은", accuracy5*100, "%입니다.")