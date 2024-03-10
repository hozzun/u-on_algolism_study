import sys
sys.setrecursionlimit(10**6)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(y, x):
    visited[y][x] = True
    for k in range(4):
        ni = y + di[k]
        nj = x + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if graph[ni][nj] and not visited[ni][nj]:
                dfs(ni, nj)


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())

    graph = [[False] * (M+1) for _ in range(N+1)]
    visited = [[False] * (M+1) for _ in range(N+1)]

    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = True

    answer = 0
    for i in range(N+1):
        for j in range(M+1):
            if graph[i][j] == True and not visited[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)
