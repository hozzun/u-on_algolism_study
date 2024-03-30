
# 백트래킹 시간초과로 실패~ -> 다익스트라로 다시 풀어보기



N = int(input())  # 노드 번호
M = int(input())  # 노선 수
adjl = [[] for _ in range(N+1)]

for _ in range(M):
    s, f, m = map(int, input().split())  # 시작, 도착, 비용
    # 단방향 그래프
    adjl[s].append((f, m))

start, finish = map(int, input().split())  # 시작도시, 도착도시
min_cost = 100000000
visited = [0] * (N+1)

def trip(C, F, M):   # 현재도시, 도착도시, 비용

    global min_cost
    if C == F:
        min_cost = min(M, min_cost)
        return
    
    if C >= min_cost:
        return

    lst = adjl[C]
    for c, m in lst:
        if not visited[c]:
            visited[c] = 1   # 방문표시
            trip(c, F, M+m)
            visited[c] = 0   # 방문표시 초기화

trip(start, finish, 0)

print(min_cost)
