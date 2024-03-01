# 64,624 kb, 222 ms

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    planet = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, -1, -1, 1, 1, 1, 0, 0]
    dj = [-1, 0, 1, -1, 0, 1, -1, 1]
    center_num = 0  # 예비후보지

    for i in range(N):
        for j in range(M):
            num = 0
            center = planet[i][j]
            for n in range(8):
                ni = i + di[n]
                nj = j + dj[n]
                # 착륙지 주변이 범위에 있고 착륙지 높이보다 낮으면 가능 지역 += 1
                if 0 <= ni < N and 0 <= nj < M and planet[ni][nj] < center:
                    num += 1
            # 가능지역 4 이상이면 예비후보지 okay~
            if num >= 4:
                center_num += 1

    print(f'#{tc} {center_num}')
