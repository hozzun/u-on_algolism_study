# 백준 2178번 미로탐색 
# 메모리 34044kb 시간 72ms 코길 533
from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(r, c):
    q = deque()
    q.append((r, c)) 

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + di[k]
            nc = c + dj[k]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1: # 범위 벗어나지 않고 1인 부분만 
                q.append((nr, nc)) # 큐에 넣음 
                arr[nr][nc] = arr[r][c] + 1 # 현재지점까지 거리는 이전 지점까지 거리  + 1 
              
    # 출발부터 도착까지 최단 경로의 길이 반환해줌 ~ 마지막 위치에 최단거리 저장된당 약간 swea 최소비용 문제 참고햇더. 
    return arr[N-1][M-1] 


print(bfs(0, 0))
