# 테게 각각 돌리면 답 나오는데 반복문 돌리니까 w, h 입력 받는 곳에서 TypeError남...;;;;;;ㅜㅜㅜㅜ
#TypeError: 'list' object is not callable

from collections import deque

di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]  # 상 하 좌 우

def bfs(v):
    Q.append(v)
    map[v[0]][v[1]] = 0
    while Q:
        r, c = Q.popleft()
        for i in range(8):
            ni = r + di[i]
            nj = c + dj[i]
            if 0 <= ni < h and 0 <= nj < w and map[ni][nj] == 1:
                Q.append((ni, nj))
                map[ni][nj] = 0

# result = []
# while True:
cnt = 0
w, h = map(int, input().split())
# if w == 0 and h == 0:
#     break
map = [list(map(int, input().split())) for _ in range(h)]

Q = deque()
for i in range(h):
    for j in range(w):
        if map[i][j] == 1:
            bfs((i, j))
            cnt += 1
print(cnt)
#     result.append(cnt)
# print(*result)
