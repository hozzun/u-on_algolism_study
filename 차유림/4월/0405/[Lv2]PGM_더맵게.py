# 프로그래머스 더 맵게 정확성 83.9 효율성 16.1
from heapq import heappush, heappop
import heapq

def solution(scoville, K):
    heapq.heapify(scoville) # 스코빌을 힙으로 바꿔줌 => 호준오빠가 알려줬음 감사링~,,
    cnt = 0 # 몇 번 섞는 지 카운트 세줄 변수 
    while scoville[0] < K and len(scoville) > 1: # K 보다 작고 길이가 1보다 클때만 while 문 돌게 함 
        heapq.heappush(scoville, (heapq.heappop(scoville) + 2 * heapq.heappop(scoville))) 
        # 인자를 두개 써야하는지 몰라서 append 썼는데 그러니까 정답 몇 개 틀렸다구 나옴!! 그래서 ai 어쩌구 해보니까 이 부분을 힙푸시 쓰는거로 고치라 해서 고쳤는데 맞음!! 
        # 가장 낮은 스코빌 지수 뽑아서 섞은다음 다시 힙에 추가함 ! 
        cnt += 1
        if len(scoville) <= 1 and scoville[0] < K: # 만약에 모든 스코빌지수를 K 이상으로 만들 수 없는 경우에는 -1 반환 
            return -1 
    return cnt
