# Python 메모리: 31452KB, 시간: 68ms, 코드 길이: 787B

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

di = [-1, -1, 0, 1, 1, 1, 0, -1] # 가로, 세로, 대각선
dj = [0, 1, 1, 1, 0, -1, -1, -1]
def dfs(y, x):
    global visited, graph
    visited[y][x] = True # 방문 처리

    for i in range(8): # 가로, 세로, 대각선 돌면서
        ni = y + di[i]
        nj = x + dj[i]
        if 0 <= ni < h and 0 <= nj < w:
            if graph[ni][nj] and not visited[ni][nj]: # 가려고 하는 가로, 세로, 대각선 중에 1이 있고, 방문 안 했다면
                dfs(ni, nj) # 이동 하면서 계속 진행

while True: # 0, 0 나올 때 까지 돌아야 하니 while문
    w, h = map(int, input().split())

    if w == 0 and h == 0: # 종료 조건
        break

    graph = [list(map(int, input().split())) for _ in range(h)] # 지도?
    visited = [[False] * w for _ in range(h)] # 방문

    answer = 0 # 정답
    for i in range(h):
        for j in range(w):
            if graph[i][j] and not visited[i][j]: # 지도를 돌면서 땅(1)이고 방문 안 했다면
                dfs(i, j) # dfs 실행
                answer += 1 # 1 증가

    print(answer) # 출력
