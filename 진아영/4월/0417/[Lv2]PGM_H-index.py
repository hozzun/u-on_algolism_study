def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(len(citations)-1, -1, -1): # 최댓값 찾아야하니까 뒤부터
        if i+1 <= citations[i]:   # 조건확인
            answer = i+1
            break
            
    return answer
