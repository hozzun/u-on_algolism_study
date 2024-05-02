# 성공 코드 -> 완전탐색했더니 시간초과 해결 못해서 딕셔너리 만들어서 중복제거

def solution(weights):
    answer = 0
    weight_dic = {}
    
    weights.sort(reverse=True) # 정렬해줘야 비율 계산 가능
    
    for weight in weights:
        if weight in weight_dic:
            # 1. 1:1인 균형 더하기
            answer += weight_dic[weight]
            # 갯수 추가
            weight_dic[weight] += 1
        else:
            # 갯수 추가
            weight_dic[weight] = 1
        
        # 2. 1:2인 균형 더하기
        if weight * 2 in weight_dic:
            answer += weight_dic[weight*2]
        # 3. 2:3인 균형 더하기
        if weight * 3 / 2 in weight_dic:
            answer += weight_dic[weight*3/2]
        # 4. 3:4인 균형 더하기
        if weight * 4 / 3 in weight_dic:
            answer += weight_dic[weight*4/3]
    
    return answer



#----------------------------------------------------------------------------------
# combinations -> 시간초과 29.4점

from itertools import combinations

def solution(weights):
    answer = 0
    
    # 균형이 맞을때
    balance = list(map(lambda x: round(x, 2), [1.0, 1/2, 2.0, 2/3, 3/2, 3/4, 4/3]))

    # 짝꿍이 가능한 모든 경우의 수
    cases = list(combinations(weights, 2))
  
    for case in cases:      
        if round(case[0] / case[1], 2) in balance:  # case의 원소들이 비율이 맞으면 
            answer += 1                             # 정답
    
    return answer

#----------------------------------------------------------------------------------------
# lambda 안에 in 조건문, slicing -> 시간초과 29.4점

from itertools import combinations

def solution(weights):
    answer = 0
    
    # 균형이 맞을때
    balance = list(map(lambda x: round(x, 2), [1.0, 1/2, 2.0, 2/3, 3/2, 3/4, 4/3]))

    for w in range(len(weights)-1):
        division = list(map(lambda x: round(x/weights[w], 2), weights[w+1:]))
        result = list(map(lambda x: x in balance, division))
        answer += result.count(True)
    
    return answer
