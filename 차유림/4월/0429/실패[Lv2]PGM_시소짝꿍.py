# 실패 버전 .. ㅠㅠ! 
from itertools import combinations
def solution(weights):
    weights.sort()
    seesaw = list(combinations(weights, 2))
    see = [1, 2, 3, 4, 3/2, 4/3]
    jjack = 0
    for i in range(len(seesaw)):
        val = seesaw[i][1] / seesaw[i][0]
        if val in see:
            jjack += 1
        
    return jjack
# -------------- 딕셔너리 사용하라는 힌트 듣고 해보는 버전..
def solution(weights):
    weights.sort()
    seesaw = [1, 2, 3, 4, 3/2, 4/3]
    cnt = 0
    jjack = {}
    for i in weights:
        if i in jjack:
            jjack[i] += 1
        else:
            jjack[i] = 1
    # for i in jjack:
    #     if 
    return jjack
