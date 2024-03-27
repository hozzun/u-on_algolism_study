# 백준 14940번 쉬운 최단거리 
from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    q = deque()
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + di[k]
            nc = c + dj[k]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0 and visited[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                visited[nr][nc] = 1
                q.append((nr, nc))           
    
    return arr

result = bfs()
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            arr[i][j] -= 2

for row in result:
    print(*row)
