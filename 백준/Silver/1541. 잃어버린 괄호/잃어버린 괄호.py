import sys
input = sys.stdin.readline

sentence = input()
l = len(sentence)-1

idx = 0
stack = list()

while idx < l:
    if sentence[idx].isdigit():
        num = int(sentence[idx])
        idx += 1

        while sentence[idx].isdigit():
            num = num*10 + int(sentence[idx])
            idx += 1
        
        while stack and stack[-1] == '+':
            stack.pop()
            num += stack.pop()

        stack.append(num)
    elif sentence[idx] == '+':
        stack.append(sentence[idx])
        idx += 1
    elif sentence[idx] == '-':
        stack.append(sentence[idx])
        idx += 1

ans = stack[0]

if len(stack) == 1:
    print(ans)
else:
    for i in range(2, len(stack), 2):
        ans -= stack[i]
    
    print(ans)