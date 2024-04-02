#정확성 69.9 효율성 30.1 ㅡㅡ..... 합계 100
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def solution(maps):
    
    def bfs(r, c, cnt): # cnt 이동 거리 카운트 
        N = len(maps)
        M = len(maps[0])
        q = deque()
        q.append((r, c, cnt))
        while q:
            r, c, cnt = q.popleft() 
            if r == N - 1 and c == M - 1: # 목적지에 도달했으면 
                return cnt # cnt 반환
            
            for k in range(4):
                nr = r + di[k]
                nc = c + dj[k]
                if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == 1:
                    q.append((nr, nc, cnt + 1))
                    maps[nr][nc] = 0
     
        return -1 # 목적지에 도달 하지 못했으면 -1 반환 
    
    answer = bfs(0, 0, 1)
    return answer
 
