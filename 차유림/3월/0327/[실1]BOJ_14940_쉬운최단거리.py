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
            if arr[i][j] == 2: # 2 인 부분 큐에넣기 
                q.append((i, j))
                visited[i][j] = 1 # 방문표시

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + di[k]
            nc = c + dj[k]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0 and visited[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1 # +1로 거리 측정
                visited[nr][nc] = 1 # 방문표시
                q.append((nr, nc))           
    
    return arr

result = bfs()
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            arr[i][j] -= 2 # -2 를 해줘서 도달 할 수 없는 곳도 알아서 -1 이 되어버려서 틀리지 않았던 거임;;;!!! 

for row in result:
    print(*row)


# ----------------------------------------------------------------------
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
                arr[i][j] = 0 # 처음 값이 계속 2로 되어있었어!!!! 0으로 안해줘서 !! 아영언니 짱 ! 

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + di[k]
            nc = c + dj[k]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0 and visited[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                visited[nr][nc] = 1
                q.append((nr, nc))           
    
    return visited

visited = bfs()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            arr[i][j] = -1 # 원래 갈 수 있는 땅인 부분 중에서 도달 할 수 없으면 -1 출력 !!!!!!! 문제를 잘 읽자..

for row in arr:
    print(*row)
