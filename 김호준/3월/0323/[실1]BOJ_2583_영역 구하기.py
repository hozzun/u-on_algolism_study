# [실1]BOJ_2583_영역 구하기
# Python 메모리: 32604KB, 시간: 56ms, 코드 길이: 922B

import sys
sys.setrecursionlimit(10**6)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(y, x):
    global cnt
    for k in range(4):
        ni = y + di[k]
        nj = x + dj[k]
        if 0 <= ni < M and 0 <= nj < N:
            if graph[ni][nj] == 0 and not visited[ni][nj]:
                cnt += 1
                visited[ni][nj] = True
                dfs(ni, nj)


M, N, K = map(int, input().split())

graph = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(M-y2, M-y1):
        for j in range(x1, x2):
            graph[i][j] = 1

arr = []
count = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and not visited[i][j]:
            cnt = 1
            visited[i][j] = True
            dfs(i, j)
            arr.append(cnt)
            count += 1

arr.sort()
print(count)
print(*arr)
