# BFS 성공 / 100점

from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    answer = 1e9
    q = deque()
    q.append((0, 0, 1))
    visited[0][0] = True
    
    while q:
        y, x, cnt = q.popleft()
        
        if y == n - 1 and x == m - 1:
            answer = min(answer, cnt)
            break
        
        for k in range(4):
            ni = y + di[k]
            nj = x + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if maps[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    q.append((ni, nj, cnt + 1))
    
    if answer == 1e9:
        return -1
    else:
        return answer

# ------------------------------------------------------------------------------------------------------------------
# DFS -> 효율성 테스트 시간초과 발생
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(maps, y, x, cnt):
    global answer, visited, n, m
    
    if cnt > answer:
        return
    
    if y == n - 1 and x == m - 1:
        answer = min(answer, cnt)
    
    for k in range(4):
        ni = y + di[k]
        nj = x + dj[k]
        if 0 <= ni < n and 0 <= nj < m:
            if maps[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = True
                dfs(maps, ni, nj, cnt + 1)
                visited[ni][nj] = False
                

def solution(maps):
    global answer, visited, n, m
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    answer = 1e9
    visited[0][0] = True
    dfs(maps, 0, 0, 1)
    
    if answer == 1e9:
        return -1
    else:
        return answer
