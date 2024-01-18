import sys
input = sys.stdin.readline

word = input()
new_word = ""

for w in word:
    if w.isupper():
        new_word += w.lower()
    else:
        new_word += w.upper()

print(new_word)