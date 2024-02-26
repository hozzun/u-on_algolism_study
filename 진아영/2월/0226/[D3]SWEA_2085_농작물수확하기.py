# 메모리 63,036 kb, 시간 238 ms

for tc in range(1, 1+int(input())):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    crops = 0

    for i in range(N // 2 + 1):

        # 농작물의 한 가운데를 지나가는 중이면
        if i == N // 2:
            crops += farm[i][N // 2]
            for j in range(1, i + 1):
                crops += farm[i][N // 2 - j]
                crops += farm[i][N // 2 + j]

        # 그렇지 않으면 위아래로 더해줌
        else:
            crops += farm[i][N//2]
            crops += farm[N - i - 1][N // 2]          # 여기

            for j in range(1, i+1):
                crops += farm[i][N//2 - j]
                crops += farm[i][N//2 + j]
                crops += farm[N - i -1][N // 2 - j]   # 여기
                crops += farm[N - i -1][N // 2 + j]   # 여기가 아랫부분

    print(f'#{tc} {crops}')
