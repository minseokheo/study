import sys
input = sys.stdin.readline

def mergeSort(A):
  if len(A) == 1:
    return A
  
  mid = (len(A)+1)//2

  left = mergeSort(A[:mid])
  right = mergeSort(A[mid:])

  i, j = 0, 0

  tmp = list()

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      tmp.append(left[i])
      answer.append(left[i])
      i+=1
    else:
      tmp.append(right[j])
      answer.append(right[j])
      j+=1
  
  while i < len(left):
    tmp.append(left[i])
    answer.append(left[i])
    i+=1
  
  while j < len(right):
    tmp.append(right[j])
    answer.append(right[j])
    j+=1
  
  return tmp

N, K = map(int, input().split())

A = list(map(int, input().split()))

answer = list()
a = list()
a = mergeSort(A)

if len(answer) >= K:
  print(answer[K-1])
else:
  print("-1")