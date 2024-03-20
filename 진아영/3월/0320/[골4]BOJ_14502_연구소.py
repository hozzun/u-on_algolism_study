# cnt가 안내려가!! 왜지? 일단 저장..

from collections import deque

# 바이러스 확산시키는 bfs함수
def virus(f, s, t, cur_lab, cnt):
    di = [0, 0, 1, -1]
    dj = [-1, 1, 0, 0]

    cnt -= 3

    cur_lab[f[0]][f[1]] = 1
    cur_lab[s[0]][s[1]] = 1
    cur_lab[t[0]][t[1]] = 1

    Q = deque()

    for r in range(N):
        for c in range(M):
            if cur_lab[r][c] == 2:
                Q.append((r, c))
    
    while Q:
        v = Q.popleft()
        for k in range(4):
            ni = v[0] + di[k]
            nj = v[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and cur_lab[ni][nj] == 0:
                cur_lab[ni][nj] = 1
                cnt -= 1
                Q.append((ni, nj))
    
    return cnt
    


N, M = map(int, input().split())   # 세로, 가로
lab = [list(map(int, input().split())) for _ in range(N)]

safe_max = 0

blank = []
blank_cnt = 0

# 빈칸 수 확인, 빈칸 위치 저장
for x in range(N):
    for y in range(M):
        if lab[x][y] == 0:
            blank.append((x, y))
            blank_cnt += 1

for a in range(blank_cnt):
    for b in range(blank_cnt):
        for c in range(blank_cnt):
            if a != b != c:
                safe = virus(blank[a], blank[b], blank[c], lab, blank_cnt)
                if safe > safe_max:
                    safe_max = safe

print(safe_max)


#-----------------------------처음에 재귀로 풀었다가 시간초과 해결 안돼서 버림--------------------------
from collections import deque
import copy

# 바이러스 확산시키는 bfs함수
def virus(i, j, cur_lab):

    visited = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append((i, j))
    visited[i][j] = 1

    while Q:
        cur = Q.popleft()
        for k in range(4):
            ni = cur[0] + di[k]
            nj = cur[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and cur_lab[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                cur_lab[ni][nj] = 2
                Q.append((ni, nj))
    return cur_lab


# 벽 세우는 재귀함수
def wall(i):
    global safe_max
    if i == 3:
        
        check_lab = copy.deepcopy(lab)
        for r in range(N):
            for c in range(M):
                if check_lab[r][c] == 2:
                    check_lab = virus(r, c, check_lab)

        safe = 0
        for a in range(N):
            for b in range(M):
                if check_lab[a][b] == 0:
                    safe += 1
                    
        if safe > safe_max:
            safe_max = safe
        return
    
    for x in range(N):
        for y in range(M):
            if lab[x][y] == 0:
                lab[x][y] = 1
                wall(i + 1)
                lab[x][y] = 0


N, M = map(int, input().split())   # 세로, 가로
lab = [list(map(int, input().split())) for _ in range(N)]

di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]
safe_max = 0

wall(0)

print(safe_max)
