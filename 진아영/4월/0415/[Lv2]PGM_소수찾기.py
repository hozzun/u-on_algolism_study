from itertools import permutations

# 소수 검사하는 함수
def check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers_list = set()  # 가능한 숫자 경우의 수
    
    for i in range(1, len(numbers)+1):
        lst = list(permutations(numbers, i))  # 모든 길이의 순열 경우의수 뽑기
        for j in lst:
            j = int(''.join(j))      # 하나씩 int로 바꾸기
            if j == 1 or j == 0:     # 1이나 0이면 소수가 아니므로 continue
                continue
            if check(j):             # 소수검사결과가 true이면
                numbers_list.add(j)  # answer 에 추가
    
    return len(numbers_list)
