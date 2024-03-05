
def bfs(i, j):
    visited[i][j] = 1  # 섬 방문표시
    q = [(i, j)]  # 큐 초기화

    while q:  # 큐가 비어있을 때까지 반복
        r, c = q.pop(0)  # 큐에서 섬의 위치를 가져옴

        for n in range(8):  # 섬 주변 탐색
            ni = r + di[n]
            nj = c + dj[n]
            if 0 <= ni < H and 0 <= nj < W and sea_map[ni][nj] and not visited[ni][nj]:  # 그 주위도 땅이라면
                visited[ni][nj] = 1  # 방문 표시
                q.append((ni, nj))   # 탐색하기 위해 큐에 저장


while True:
    W, H = map(int, input().split())  # 너비 W, 높이 H
    if not W and not H:
        break

    sea_map = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]  # 각 테스트 케이스마다 visited 배열 초기화
    di = [1, 1, 1, 0, 0, -1, -1, -1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    island = 0
    for r in range(H):
        for c in range(W):
            if sea_map[r][c] and not visited[r][c]:   # 지도를 전부 확인하면서 땅이면서 방문안한곳 깊이우선탐색
                island += 1
                bfs(r, c)
    print(island)
