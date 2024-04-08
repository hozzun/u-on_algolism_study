while로 다시 해볼게 ~~~


# --------------------------------------------------------------------------------------------------------
# 처음에 재귀로 풀었는데 채점결과 테케 하나 틀림..

from heapq import heappop, heappush, heapify
answer = 0

def solution(scoville, K):
    global answer
    heapify(scoville)

    if scoville[0] >= K:
        return
    
    elif len(scoville) <= 1 and scoville[0] < K:
        answer = -1
        return

    new = heappop(scoville) + heappop(scoville) * 2
    heappush(scoville, new)
    answer += 1
    solution(scoville, K)
    return answer
