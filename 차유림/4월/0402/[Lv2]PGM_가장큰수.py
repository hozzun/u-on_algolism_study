# 26.7 점 실화야?~?~?!?!!? ㅜ 졸려서 일단 잔다~~~ 

from itertools import permutations

def solution(numbers):
    string = ''
    for i in numbers:
        string += str(i)
    
    result = list(permutations(numbers, len(numbers)))
    real = []
    for num in result:
        digit = int(''.join(map(str, num)))
        real.append(digit)
                  
    real_val = max(real)
    return str(real_val)
