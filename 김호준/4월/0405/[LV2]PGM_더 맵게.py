# 100점

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 스코빌 힙으로 바꿔줌
    
    while True:
        if len(scoville) == 1 and scoville[0] < K: # 만약 모든 스코빌을 돌렸는데, K 이상이 안되면
            return -1 # -1 출력
        
        else:
            flag = 0 # 브레이크용
            for i in range(len(scoville)):
                if scoville[i] < K: # 만약 i번째 값이 K보다 작으면
                    result = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2) # 계산
                    heapq.heappush(scoville, result) # 다시 넣어줌
                    answer += 1 # 카운트 1 증가
                    break # 다시 첨부터 돌리기
                else:
                    flag += 1 # i번째 값이 K보다 크면 1씩 증가
                    if flag == len(scoville): # 스코빌 모두 K보다 크면
                        return answer # 이제껏 카운트 출력
