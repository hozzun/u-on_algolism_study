# Python 메모리: 149796KB, 시간: 1052ms, 코드 길이: 593B

import sys
sys.setrecursionlimit(10**6)

di = [1, 0, -1, 0] # 상 하 좌 우
dj = [0, 1, 0, -1]
def dfs(y, x): # dfs
    visited[y][x] = True
    for k in range(4):
        ni = y + di[k]
        nj = x + dj[k]
        if 0 <= ni < M and 0 <= nj < N:
            if graph[ni][nj] == 0 and not visited[ni][nj]:
                dfs(ni, nj)


M, N = map(int, input().split())

graph = [list(map(int, input())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for i in range(N):
    if graph[0][i] == 0 and not visited[0][i]: # 첫번 째 줄에서 시작해서 끝에 도달하는가로 찾음
        dfs(0, i)

if True in visited[M-1]: # 끝에 도달 했으면 YES 아니면 NO
    print('YES')
else:
    print('NO')
