# 메모리초과로 실패 -> 집가서 수정해보려고 여기 일단 저장~

import sys
sys.setrecursionlimit(100000)

def dfs(i, j, h):
    visited[i][j] = 1

    for n in range(4):
        ni = i + di[n]
        nj = j + dj[n]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and ground[ni][nj] > h:
            dfs(ni, nj, h)


N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]
max_safe_area = 0
max_high = max(map(max, ground))
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


for high in range(1, max_high + 1):
    visited = [[0] * N for _ in range(N)]
    safe_area = 0
    for r in range(N):
        for c in range(N):
            if ground[r][c] > high and not visited[r][c]:
                dfs(r, c, high)
                safe_area += 1
    if safe_area > max_safe_area:
        max_safe_area = safe_area

print(max_safe_area)

