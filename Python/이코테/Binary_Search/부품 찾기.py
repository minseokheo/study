import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

def binary_search(target, array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    
    if target < array[mid]:
        return binary_search(target, array, start, mid-1)
    elif target == array[mid]:
        return mid
    else:
        return binary_search(target, array, mid+1, end)

for num in b:
    result = binary_search(num, a, 0, n-1)

    if result == None:
       print("no", end = " ")
    else:
      print("yes", end = " ")