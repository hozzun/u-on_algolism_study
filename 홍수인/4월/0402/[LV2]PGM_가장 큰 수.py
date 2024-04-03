# 26.7점 시간초과..ㅎㅎ 다른 방법이 생각이 안남 ..ㅜㅜ

from itertools import permutations

def solution(numbers):
    max_val = 0
    for n in permutations(numbers, len(numbers)):
        answer = ''
        for i in n:
            answer += str(i)
        max_val = max(int(answer), max_val)
    return str(max_val)
