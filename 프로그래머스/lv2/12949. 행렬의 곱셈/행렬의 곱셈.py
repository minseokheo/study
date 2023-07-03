import numpy as np

def solution(arr1, arr2):
    answer = [[]]
    a1 = np.array(arr1)
    a2 = np.array(arr2)
    a = a1 @ a2
    return a.tolist()