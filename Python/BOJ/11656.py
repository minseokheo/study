import sys
input = sys.stdin.readline

string = input().rstrip()
string_list = []

for i in range(len(string)):
  string_list.append(string[i:])

string_list.sort()
print(*string_list)