# ALL 시간초과 조졌다 (일단 보류)

from itertools import permutations

def solution(numbers):
    answer = 0
    for i in permutations(numbers, len(numbers)):
        result = ''
        for j in i:
            result += str(j)
        
        if int(result) >= answer:
            answer = int(result)
    
    return str(answer)
