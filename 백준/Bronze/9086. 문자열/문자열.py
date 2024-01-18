import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    new_word = ""
    word = input().rstrip()
    new_word = word[0] + word[-1]
    print(new_word)