메모리 : 33188kb , 시간 : 60ms, 코드 길이 : 267B

from heapq import heappush, heappop, heapify

n, m = map(int, input().split())
status = list(map(int, input().split()))
heapify(status)    # heap으로 변환

for i in range(m):
    r = heappop(status) + heappop(status)   # 최소값 두개 더한 값
    for _ in range(2):    # 두 카드 모두 더한 결과로 바꿈
        heappush(status, r)
print(sum(status))
