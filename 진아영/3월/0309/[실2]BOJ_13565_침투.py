# 124948KB 272ms

from collections import deque

def percolate(r, c):
    q = deque()
        
    figure[r][c] = 2   # 방문표시
    q.append((r, c))

    while q:
        a = q.popleft()
        for n in range(4):
            ni = a[0] + di[n]
            nj = a[1] + dj[n]
            if 0 <= ni < M and 0 <= nj < N and figure[ni][nj] == 0:   # 전류가 통하는 구간이면
                figure[ni][nj] = 2                                    # 방문표시
                q.append((ni, nj))

M, N = map(int, input().split())  # 세로, 가로
figure = [list(map(int, input())) for _ in range(M)]
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for i in range(N):
    if figure[0][i] == 0:   # 제일 바깥쪽에 전류가 통하는 길이 있으면 거기부터 시작
        percolate(0, i)

# 제일 안쪽에 전류가 통한 흔적이 있으면 YES
if 2 in figure[M-1]:
    print('YES')
else:
    print('NO')
