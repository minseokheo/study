import sys
input = sys.stdin.readline

alpha = [0 for i in range(26)]

word = list(input().rstrip())

for alphabet in word:
  alpha[ord(alphabet)-97] += 1

print(*alpha)