# 완전탐색으로 구했더니 메모리 초과... 흠~ 더 고민해보겠어~~~ 실버2라 뭔가 더 간단한 방법이 있을거같은데~~~~~~~~~~

from itertools import permutations

def check(num):
    for n in range(2, num):
        if num % n != 0:
            continue
        else:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    candidate = set()
    for i in range(len(numbers)):
        lst = list(permutations(numbers, i))
        for j in lst:
            candidate.add(int(j))
    candidate = list(candidate)
    for k in candidate:
        if check(k):
            answer += 1
    return answer
