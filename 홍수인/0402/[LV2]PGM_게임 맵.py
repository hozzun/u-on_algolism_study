 # 1 == 길
from collections import deque

def solution(maps):
    ans = -1
    Q = deque()
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    
    visited[0][0] == 1     # 시작점 방문표시
    Q.append((0, 0, 1))    # 행, 열, 거리
    
    while Q:
        r, c, dis = Q.popleft()
        if r == n-1 and c == m-1:   # 목적지 도달 시 ans에 dis 할당한 후 종료
            ans = dis
            break
            
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        
        for i in range(4):   # 네방향
            ni = r + di[i]
            nj = c + dj[i]
            if 0 <= ni < n and 0 <= nj < m:
                if maps[ni][nj] == 1 and visited[ni][nj] == 0:   # 길이고, 방문하지 않은 곳이라면 Q.append , dis값 누적
                    Q.append((ni, nj, dis+1))
                    visited[ni][nj] = 1
    return ans
