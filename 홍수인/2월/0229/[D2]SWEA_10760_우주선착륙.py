# 메모리 64628 / 시간 226ms

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    # 우, 좌, 우상, 좌상, 하, 우하, 좌하, 상 (8방향 delta)
    di = [0, 0, 1, 1, 1, -1, -1, -1]
    dj = [1, -1, 1, -1, 0, 1, -1, 0]

    for i in range(n):
        for j in range(m):
            center = arr[i][j]
            cnt = 0

            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] < center:
                    cnt += 1    # center 기준 지대가 낮은 곳의 수 
            if cnt >= 4:   # center보다 지대가 낮은 곳의 수가 4이상이면 result ++1
                result += 1
                
    print(f'#{tc} {result}')
