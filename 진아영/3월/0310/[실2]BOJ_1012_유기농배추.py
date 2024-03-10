# 31484 KB, 304 ms

import sys
sys.setrecursionlimit(1000000)


def find_warm(a, b):
    farm[a][b] = 0   # 방문표시

    for k in range(4):
        na = a + di[k]
        nb = b + dj[k]
        if 0 <= na < N and 0 <= nb < M and farm[na][nb]:
            find_warm(na, nb)


for tc in range(1, 1+int(input())):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추위치의 개수
    farm = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    warm = 0

    for i in range(N):
        for j in range(M):
            if farm[i][j]:
                warm += 1
                find_warm(i, j)

    print(warm)
