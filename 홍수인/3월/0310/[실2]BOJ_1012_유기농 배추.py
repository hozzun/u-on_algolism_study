메모리 : 34072, 시간 : 324ms, 코드 길이 : 33

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]   # 상 하 좌 우

def bfs(r, c):
    Q.append((r, c))
    graph[r][c] = 0
    while Q:
        a, b = Q.popleft()
        for i in range(4):
            ni = a + di[i]
            nj = b + dj[i]
            if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 1:
                Q.append((ni, nj))
                graph[ni][nj] = 0

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())  # 가로, 세로, 위치
    graph = [[0] * m for _ in range(n)]
    cnt = 0

    for i in range(k):    # 그래프 형성
        y, x = map(int, input().split())
        graph[x][y] = 1

    Q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
