# Python 메모리: 38412KB, 시간: 560ms, 코드 길이: 518B

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 메모리 풀어줌

def dfs(x): # dfs
    visited[x] = True
    for i in range(1, N+1):
        if not visited[i] and graph[x][i]:
            dfs(i)


N, M = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True # 양방향
    graph[v][u] = True

visited = [False] * (N+1) # 방문

cnt = 0
for i in range(1, N+1): # 1~N까지 dfs 돌면서 1씩 증가
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
