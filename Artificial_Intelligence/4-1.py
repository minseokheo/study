from sklearn.linear_model import Perceptron


X = [[0,0],[0,1],[1,0],[1,1]]
y = [-1,1,1,1]


p = Perceptron()
p.fit(X,y)

print(p.coef_, p.intercept_)
print(p.predict(X))
print(p.score(X,y)*100, "%")