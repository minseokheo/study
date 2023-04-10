from sklearn import datasets
from sklearn import svm, tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
import numpy as np

digit=datasets.load_digits()
x_train,x_test,y_train,y_test=train_test_split(digit.data,digit.target,train_size=0.6) # 40%를 테스트 집합으로 함

################
# 본인 코드 작성
################
s = svm.SVC(gamma=0.001)
accuracies_svm = cross_val_score(s, digit.data, digit.target, cv=5)
print("SVM 정확률(평균)=%0.3f, 표준편차=%0.3f" %(accuracies_svm.mean()*100,accuracies_svm.std()))

t = tree.DecisionTreeClassifier()
accuracies_tree = cross_val_score(t, digit.data, digit.target, cv=5)
print("DecisionTree 정확률(평균)=%0.3f, 표준편차=%0.3f" %(accuracies_tree.mean()*100,accuracies_tree.std()))

rf = RandomForestClassifier()
accuracies_rf = cross_val_score(rf, digit.data, digit.target, cv=5)
print("RandomForest 정확률(평균)=%0.3f, 표준편차=%0.3f" %(accuracies_rf.mean()*100,accuracies_rf.std()))

s.fit(x_train, y_train)
res = s.predict(x_test)

conf = np.zeros((10,10))
for i in range(len(res)):
    conf[res[i]][y_test[i]] += 1
print(conf)

no_correct = 0
for i in range(10):
    no_correct += conf[i][i]
accuracy = no_correct / len(res)
print("테스트 집합에 대한 정확률은", accuracy*100,"%입니다.")