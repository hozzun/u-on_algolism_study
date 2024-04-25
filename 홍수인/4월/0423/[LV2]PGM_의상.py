def solution(clothes):
    answer = 0
    dic = {}
    
    # 카테고리 별로 분류하여 딕셔너리에 저장
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1

    # 모든 경우의 수 구하기
    ans = 1
    for i in dic.values():
        ans *= (i+1)
    answer = ans -1   # 아무것도 고르지 않는 경우 -1
        
    return answer
