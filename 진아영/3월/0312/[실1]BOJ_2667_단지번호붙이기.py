# 	34072 KB, 72 ms, 807 B


from collections import deque

def number(i, j):
    q = deque()
    q.append((i, j))
    apartment[i][j] = 0  # 방문표시
    num = 1  # 단지 번호

    while q:
        a = q.popleft()
        for n in range(4):
            ni = a[0] + di[n]
            nj = a[1] + dj[n]
            if 0 <= ni < N and 0 <= nj < N and apartment[ni][nj]:
                apartment[ni][nj] = 0
                q.append((ni, nj))
                num += 1
    return num


N = int(input())
apartment = [list(map(int, input())) for _ in range(N)]
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
apartment_number = []
cnt = 0

for r in range(N):
    for c in range(N):
        if apartment[r][c]:
            cnt += 1
            a = number(r, c)  # a : 단지번호
            apartment_number.append(a)

print(cnt)   # 단지 수
for n in sorted(apartment_number):   # 정렬해서 단지번호 출력
    print(n)
