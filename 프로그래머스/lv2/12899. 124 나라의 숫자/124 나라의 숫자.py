# 문제에 대한 첫 접근 1, 2, 4가 반복된다는 점으로 보아 3으로 나누었을 때의 몫과 나머지를 이용하는 것으로 생각
# 노트에 적어서 몇번 해보니 규칙이 있다는 것을 발견하였고 그 규칙을 토대로 프로그래밍 해보려함
def solution(n):
    """
    d = ['0', '1', '2', '4']
    if n >= 4:
        for i in range(4, n+1):
            if i % 3 == 1:
                d.append(d[i//3] + '1')
            elif i % 3 == 2:
                d.append(d[i//3] + '2')
            elif i % 3 == 0:
                d.append(d[(i//3)-1] + '4')
    """
    # 위의 코드로 풀었을때는 테스트케이스는 모두 통과하지만 시간복잡도가 모두 초과해버림
    # 데이터의 갯수가 5천만개인데 O(n)으로 동작해서 그런듯함
    # 규칙을 dp를 이용해서 풀지않고 숫자를 받으면 바로 동작하도록 고민해봐야겠음
    answer = ''
    while n != 0:
        if n % 3 == 1:
            answer = '1' + answer
            n = n // 3
        elif n % 3 == 2:
            answer = '2' + answer
            n = n // 3
        elif n % 3 == 0:
            answer = '4' + answer
            n = n // 3 - 1
    return answer