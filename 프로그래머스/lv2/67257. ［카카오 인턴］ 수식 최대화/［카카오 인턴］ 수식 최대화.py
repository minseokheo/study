# 최초로 생각해낸 생각은 연산자가 2개일때와 3개일때로 나누고
# 2개일때는 2가지 경우, 3개일때는 6가지 경우가 나오므로
# 모두 계산해서 절댓값이 큰 것을 return하면 되겠다는 생각이 들었습니다.
from itertools import permutations

def calculate(operator, index, operand):
    if operator == '+':
        return operand[index] + operand[index+1]
    elif operator == '-':
        return operand[index] - operand[index+1]
    elif operator == '*':
        return operand[index] * operand[index+1]

def solution(expression):
    answer = -1
    operand = []
    operator = []
    num = ""
    
    # 우선 expression을 뜯어서 operand와 operator를 구분합니다.
    for i in range(len(expression)):
        if expression[i].isdigit():
            num += expression[i]
        else:
            operator.append(expression[i])
            operand.append(int(num))
            num = ""
    operand.append(int(num))
    # print(operand)
    # print(operator)
    
    # set을 이용해서 operator의 갯수를 파악하고 순열을 이용해 경우의 수를 계산해 줍니다.
    set_operator = set(operator)
    op_count = len(set_operator)
    op_order = []
    
    for x in permutations(set_operator, op_count):
        op_order.append(x)
    # print(op_order)
    
    # 경우의 수 만큼 for문을 돌리고
    for order in op_order:
        operand_copy = operand.copy()
        operator_copy = operator.copy()
        # 해당 경우에서의 연산자들을 for문을 돌리고
        for op in order:
            i = 0
            while True:
                if i >= len(operator_copy):
                    break
                if op == operator_copy[i]:
                    # calculate 함수를 사용한 이유는 op값이 +인지 -인지 *인지 알 수 없기 때문에
                    # 간단하게 만들기 위해 함수를 만들었습니다.
                    operand_copy[i] = calculate(op, i, operand_copy)
                    operator_copy.pop(i)
                    operand_copy.pop(i+1)
                    # print(operand_copy)
                    # print(operator_copy)
                    continue
                i += 1
        if answer < abs(operand_copy[0]):
            answer = abs(operand_copy[0])
    return answer