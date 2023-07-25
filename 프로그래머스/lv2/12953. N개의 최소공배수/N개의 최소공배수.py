import math

def lcm(a, b):
    return a*b // math.gcd(a,b)

def solution(arr):
    stack = []
    
    for num in arr:
        if not stack:
            stack.append(num)
        else:
            stack.append(lcm(stack.pop(), num))
            
    return stack[-1]