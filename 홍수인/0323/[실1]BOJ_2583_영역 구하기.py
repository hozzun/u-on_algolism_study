import sys
sys.setrecursionlimit(10**6)
di = [1, 0, -1, 0]  # 상하좌우
dj = [0, 1, 0, -1]

def find(r, c):
    global cnt
    for i in range(4):
        ni = c + di[i]   # x좌표
        nj = r + dj[i]   # y좌표
        if 0 <= ni < n and 0 <= nj < m and graph[nj][ni] == 0:
            graph[nj][ni] = 1
            cnt += 1   # 한 영역의 넓이
            find(nj, ni)
    return

m, n, k = map(int, input().split())
r_lst = []   # k개의 영역들의 넓이 저장
graph = [[0] * n for _ in range(m)]  # n: 가로, m: 세로

for _ in range(k):
    a = list(map(int, input().split()))
    for i in range(a[1], a[3]):
        for j in range(a[0], a[2]):
            graph[i][j] = 1

result = 0
cnt_lst = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt = 0
            graph[i][j] = 0
            find(i, j)
            cnt_lst.append(cnt)
            result += 1  # 영역의 개수
cnt_lst.sort()
print(result)
print(*cnt_lst)
