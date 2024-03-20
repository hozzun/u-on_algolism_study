# PyPy3, 메모리: 127088KB, 시간: 2628ms, 코드 길이: 1114B
# Python은 시간초과 나더라
from collections import deque
import copy

di = [1, 0, -1, 0] # 상하좌우
dj = [0, 1, 0, -1]

def wall(cnt): # 벽 만들어주는 함수
    if cnt == 3: # 벽 3개가 되면
        bfs() # 바이러스 퍼트려봐라
        return

    for i in range(N):
        for j in range(M):
            if wall_graph[i][j] == 0: # 길이면
                wall_graph[i][j] = 1 # 벽 세워봐
                wall(cnt + 1) # 횟수 1 증가
                wall_graph[i][j] = 0 # 백트래킹

def bfs(): # bfs로 바이러스 터트리는 함수
    global answer
    graph = copy.deepcopy(wall_graph)
    # 원래 그래프에 해봤는데, 계속 벽 3개 만들면서 시도해봐야해서 똑같은거 카피로 가져옴
    # (카피는 찾아봄)

    q = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2: # 바이러스 찾고
                q.append((i, j))

    while q: # 바이러스 퍼트림
        y, x = q.popleft()
        for k in range(4):
            ni = y + di[k]
            nj = x + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj] == 0: # 상하좌우에 0 있으면
                    graph[ni][nj] = 2 # 2로 바꾸고 이동
                    q.append((ni, nj))

    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0: # 바이러스 다 퍼트리고 0 남은거 몇갠지 세주기
                result += 1

    answer = max(result, answer) # 계속 벽 3개씩 세워보면서 최대 값 찾기


N, M = map(int, input().split())
wall_graph = [list(map(int, input().split())) for _ in range(N)]

answer = 0
wall(0)

print(answer)
