# 117716 KB, 192 ms


def dfs(i, j):
    visited[i][j] = 1

    for n in range(8):   # 주위 8구역 땅인지 탐색
        ni = i + di[n]
        nj = j + dj[n]
        if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj] and sea_map[ni][nj]:   # 방문하지 않은 곳이고 땅이면
            dfs(ni, nj)


while True:

    try:
        W, H = map(int, input().split())
        sea_map = [list(map(int, input().split())) for _ in range(H)]
        visited = [[0] * W for _ in range(H)]
        island = 0
        di = [1, 1, 1, 0, 0, -1, -1, -1]
        dj = [-1, 0, 1, -1, 1, -1, 0, 1]

        if W or H:     # w랑 h 0인 이상한 테케 주어지길래 이렇게 함
            for r in range(H):
                for c in range(W):
                    if not visited[r][c] and sea_map[r][c]:    # 지도 다 보면서 땅인곳 깊이우선탐색
                        dfs(r, c)
                        island += 1
            print(island)

    except EOFError:   # 테케 수 주어지지 않았을 때 인풋 없으면 예외처리
        break
