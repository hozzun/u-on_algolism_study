# 시간초과
# 우리 실습 SWEA 그래프_최소 이동 거리랑 똑같이 풀긴함
# 다익스트라(최소힙)
# 모르겠다 ~

import sys
import heapq

input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [1e9] * (N+1)

for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append([e, cost])

start, end = map(int, input().split())

q = []
visited[start] = 0
heapq.heappush(q, [0, start])

while q:
    A, B = heapq.heappop(q)

    for nxt, nxt_cost in graph[B]:
        if visited[nxt] > visited[B] + nxt_cost:
            visited[nxt] = visited[B] + nxt_cost
            heapq.heappush(q, [visited[nxt], nxt])

print(visited[end])
