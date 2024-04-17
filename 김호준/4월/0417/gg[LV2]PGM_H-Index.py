# 뭔소린지 모르겠다~
# 6.3점 ㅋㅋ

def solution(citations):
    answer = 0
    citations.sort()
    
    for i in citations:
        more = 0
        less = 0
        for j in citations:
            if j >= i:
                more += 1
            elif j < i:
                less += 1
        
        if more == i:
            answer = max(answer, i)
            
    return answer
