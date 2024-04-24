# 의상 해쉬 => 딕셔너리 ~!~!~! 
# 딕셔너리 만드는건 메뉴리뉴얼 할떄처럼 만들었음~!!! 

def solution(clothes):
    answer = 1
    comb = {} # 딕셔너리 만들어줌 종류별로 묶어서
    for clothes, type in clothes:
        if type in comb:
            comb[type] += 1
        else:
            comb[type] = 1
            
    # print(comb)       
    
    for value in comb.values():
        answer *= (value + 1) 
  
        # headgear 선택 (2개) + headgear 아예 선택하지 않는 경우의 수 (1개) = 3개
        # eyewear 선택 (1개) + eyewear 아예 선택하지 않는 경우의 수 (1개) = 2개   곱해주면 됨
        
    return answer - 1 # 의상 무조건 1개 이상 입어야 하므로 head x - eye x 의 경우의 수 1개는 뺴줘야함

# head 1    # eye 1
# head 2    # eye x 
# head X   
