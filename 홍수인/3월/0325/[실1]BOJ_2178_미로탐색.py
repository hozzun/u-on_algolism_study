# 메모리: 34204KB, 시간: 80ms, 코드 길이: 858B

from collections import deque

def bfs(r, c, cnt):
    global result
    Q = deque()
    Q.append((r, c, cnt))
    visited[r][c] = 1

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while Q:
        q = Q.popleft()
        for i in range(4):
            ni = q[0] + di[i]  # 행
            nj = q[1] + dj[i]  # 열
            if 0 <= ni < n and 0 <= nj < m:
                if visited[ni][nj] == 0 and graph[ni][nj] == 1:  # 방문하지 않고 길이라면
                    if ni == n-1 and nj == m-1:   # 목적지 도달
                        result = q[2] + 1
                    visited[ni][nj] = 1
                    Q.append((ni, nj, q[2] + 1))

n, m = map(int, input().split())   # n: 세로, m: 가로
graph = [[int(i) for i in input()] for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = 99999999
bfs(0, 0, 1)
print(result)
