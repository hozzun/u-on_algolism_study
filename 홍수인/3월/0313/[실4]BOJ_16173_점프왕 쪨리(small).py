# 메모리 : 31120kb, 시간 : 44ms, 코드 길이 : 573B

di = [0, 1]
dj = [1, 0]  # 우, 하

def dfs(r, c, val):
    global result
    if graph[r][c] == -1:   # 도착점(-1)에 도달
        result = 'HaruHaru'
        return

    graph[r][c] = 0  # 방문 표시 0으로 변경.
    for i in range(2):
        ni = r + di[i] * val
        nj = c + dj[i] * val
        # graph 범위 내 & 방문하지 않은 곳이라면
        if 0 <= ni < n and 0 <= nj < n and graph[ni][nj] != 0:
            dfs(ni, nj, graph[ni][nj])
    else:   # 양방향 모두 조건에 맞지 않다면 돌아감.
        return

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 'Hing'
dfs(0, 0, graph[0][0])
print(result)
