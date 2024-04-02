# 100점

from collections import deque

def game(arr, m, n):   # 맵 배열, 세로, 가로
    
    Q = deque()
    Q.append((0, 0))
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    
    while Q:
        x, y = Q.popleft()
        if x == m-1 and y == n-1:
            return arr[x][y]   # 거기까지의 거리 return
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0<= ni < m and 0 <= nj < n and arr[ni][nj] == 1:
                Q.append((ni, nj))
                arr[ni][nj] += arr[x][y]  # 거리 누적
                
    return -1  # 실패시 -1 return
    
def solution(maps):
    answer = 0
    M = len(maps)    # 세로
    N = len(maps[0]) # 가로
    answer = game(maps, M, N)
    
    return answer
