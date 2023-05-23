from sklearn import datasets

d = datasets.load_iris()            # iris 데이터셋을 읽고
#print(d.DESCR)                      # 내용을 출력
for i in range(0, len(d.data)):     # 샘플을 순서대로 출력
    print(i+1, d.data[i], d.target[i])