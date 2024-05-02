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
