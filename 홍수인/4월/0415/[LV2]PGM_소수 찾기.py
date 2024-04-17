# 100
# 시간 초과 나서 딕셔너리로 바꾸고 p_lst에 넣을 때 조건 추가해서 짝수, 0, 1 은 제외.
# while문 나누는 값인 i를 val - 1을 초기값으로 감소하는 방향으로 소수 판별하도록 했는데 이거 초기값 3부터 증가하는 방향으로 하니까 통과함

from itertools import permutations

def solution(numbers):
    answer = 0
    p_lst = {}
    
    # 순열 만들기
    for i in range(1, len(numbers)+1):
        for n in permutations(numbers, i):
            num = ''.join(n)
            if int(num) > 1 and int(num) not in p_lst:
                if int(num)%2 == 1 or int(num) == 2:
                    p_lst[int(num)] = 1

    for val in p_lst:
        i = 2
        flag = True
        while i < val :
            if val % i == 0:   # 나누어 떨어지면 소수 아님
                flag = False
                break
            i += 1
        if flag == True:    # while 끝날 때 까지 나누어지는 수가 없었으면 소수. => answer += 1
            answer += 1
    return answer
