from itertools import combinations
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
a = sorted(list(map(str, input().split())))
ans = list()
vowel = ['a', 'e', 'i', 'o', 'u']

for s in combinations(a, L):
    vo = 0
    for i in s:
        if i in vowel:
            vo += 1
    
    if vo >= 1 and L - vo >= 2:
        print(''.join(s))