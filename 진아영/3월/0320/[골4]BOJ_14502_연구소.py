# 맨 첨에 N * N 으로 착각하고 제출했다가 자꾸 7프로에서 멈춰서 두시간 날림... 나 너무 힘들어~
# 파이파이 141188 KB, 6448 ms, 1446 B


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
    if i == 3:    # 벽 세개 다 세웠으면 그때의 실험실로 bfs 돌아줌
        
        check_lab = copy.deepcopy(lab)    # 첨에 그냥 check_lab = lab으로 했더니 초기화가 안돼서 딥카피 해줌
        for r in range(N):
            for c in range(M):
                if check_lab[r][c] == 2:
                    check_lab = virus(r, c, check_lab)     # virus 확산시키기
                    
        safe = 0      # 안전구역 세주기
        for a in range(N):
            for b in range(M):
                if check_lab[a][b] == 0:
                    safe += 1
                    
        if safe > safe_max:     # 최댓값 갱신
            safe_max = safe
        return

    for x in range(N):
        for y in range(M):
            if lab[x][y] == 0:    # 빈공간에
                lab[x][y] = 1     # 벽 세우고
                wall(i + 1)       # 재귀
                lab[x][y] = 0     # 벽 허물기


N, M = map(int, input().split())   # 세로, 가로
lab = [list(map(int, input().split())) for _ in range(N)]

di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]
safe_max = 0

wall(0)

print(safe_max)
