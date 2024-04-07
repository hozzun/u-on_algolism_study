# 100점 -> 수정전 시간초과나서 min함수 수정
# 수정전 : 주석처리, 수정후 : 주석 밑 코드

from heapq import heappop, heappush, heapify

def solution(scoville, K):
    answer = 0
    # heap_s = []
    
    # 힙큐에 push
    # for i in scoville:
    #     heappush(heap_s, i)
    heapify(scoville)
    
    # while min(scoville) < K and len(scoville) >= 2:
    while scoville[0] < K and len(scoville) >= 2:

        first = heappop(scoville)
        second = heappop(scoville)
        heappush(scoville, first + second * 2)
        answer += 1
    
    # if min(scoville) < K:
    if scoville[0] < K:
        answer = -1
        
    return answer
