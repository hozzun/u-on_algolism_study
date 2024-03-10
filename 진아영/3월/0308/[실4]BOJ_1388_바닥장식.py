# 파이썬 34072 KB, 68 ms
# 파이파이 114284 KB, 156 ms


from collections import deque

def check_deck(i, j):
    q = deque()
    cur_shape = floor[i][j]   # 모양 저장
    floor[i][j] = 0           # 방문표시
    q.append((i, j))

    while q:
        a = q.popleft()
        if cur_shape == '-':    # 가로 장식이면
            ni = a[0]           # 가로 탐색
            nj = a[1] + 1
        elif cur_shape == '|':  # 세로 장식이면
            ni = a[0] + 1       # 세로 탐색
            nj = a[1]

        if 0 <= ni < N and 0 <= nj < M and floor[ni][nj] == cur_shape:   # 탐색할 모양이랑 같으면
            floor[ni][nj] = 0                                            # 방문표시하고
            q.append((ni, nj))                                           # 탐색할 q에 append


N, M = map(int, input().split())   # 세로, 가로
floor = [list(input()) for _ in range(N)]

deck = 0

for r in range(N):
    for c in range(M):
        if floor[r][c]:   # 방문하지 않은 곳이면
            deck += 1     # 장식 개수 추가해주고
            check_deck(r, c)    # 너비우선탐색

print(deck)

