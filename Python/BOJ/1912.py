"""
    10, -4, 3, 1, 5, 6, -35, 12, 21, -1
    12, 21 -> 33
"""

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [a[0]]

for i in range(n-1):
    d.append(max(d[i] + a[i+1], a[i+1]))

print(max(d))