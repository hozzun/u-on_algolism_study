# 메모리: 62,796KB, 시간: 203ms

di = [1, -1, 0, 0, -1, 1, -1, 1]
# 아래, 위, 우, 좌, 좌상, 우하, 우상, 좌하
dj = [0, 0, 1, -1, -1, 1, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                ni = i + di[k] # 주변 8개 돌기
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[i][j] > arr[ni][nj]: # 만약 주변 값이 더 작으면 카운트 1 증가
                        cnt += 1
            if cnt >= 4: # 4개 이상이면
                answer += 1 # 개수 1개 증가

    print(f'#{tc}', answer) # 출력
