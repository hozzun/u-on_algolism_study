# pypy, 메모리: 139044, 시간: 2876ms, 코드 길이: 1522B
# python 시간초과

import copy
from collections import deque
import sys
input = sys.stdin.readline

def wall(wall_cnt):
    if wall_cnt == 3:  # 벽 세개 세우면
        bfs()   # 바이러스 퍼뜨리는 함수 실행.
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:  # 0이라면 벽세움
                graph[i][j] = 1
                wall(wall_cnt + 1)   # 벽의 수 +1
                graph[i][j] = 0

di = [1, 0, -1, 0]  # 상하좌우
dj = [0, 1, 0, -1]

def bfs():   # 바이러스 확산시키는 함수
    global r_result
    global r_lst
    virus_graph = copy.deepcopy(graph)   # 바이러스 확산시킨 그래프

    Q = deque()
    for i in range(n):
        for j in range(m):
            if virus_graph[i][j] == 2:
                Q.append((i, j))

    while Q:   # 바이러스 확산시킴
        r, c = Q.popleft()
        for i in range(4):
            ni = r + di[i]
            nj = c + dj[i]
            if 0 <= ni < n and 0 <= nj < m:
                if virus_graph[ni][nj] == 0:  # 주변에 0이 있으면 2로바꿈
                    virus_graph[ni][nj] = 2
                    Q.append((ni, nj))

    result = 0
    for i in range(n):   # 안전영역 수 세기
        for j in range(m):
            if virus_graph[i][j] == 0:
                result += 1
    r_lst.append(result)   # 안전영역 최대값 찾기


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
r_lst = []
wall(0)
print(max(r_lst))
