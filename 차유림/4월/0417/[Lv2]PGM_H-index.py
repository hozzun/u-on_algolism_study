# H-index
# 위키백과 링크된거 내용 보고 풀었음ㅠㅠ !
# f 가 해당 위치보다 크거나 같은 마지막 위치를 찾아야 한다고 하는 거 보고 풀었음 !! 

def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    h = 0
    for i in range(n):
        if citations[i] >= i + 1: # 첫번쨰 위치에 있는 값(6) 이 1 보다 크거나 같으면 
            h = i + 1 # h 는 1 
            # 이런 식으로 쭉쭉 2번째 위치 값 (5) 가 2보다 크거나 같으면 h 는 2 
            # 3번째 위치 값 (3) 이 3보다 크거나 같으면 h 는 3 
        
    return h # h 는 3! 
