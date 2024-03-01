# swea 10760번 우주선 착륙2 메모리 64,892kb, 시간 228ms 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    arr = [list(map(int, input().split())) for _ in range(N)]
    goal = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] < arr[i][j]: # arr[i][j] < arr[ni][nj] <- 아니 낮은 걸 찾아야 하는데 높은 걸 찾고 있었음 !!!! 바보. 
                        cnt += 1
            if cnt >= 4:
                goal += 1
    
    print(f"#{tc} {goal}")
