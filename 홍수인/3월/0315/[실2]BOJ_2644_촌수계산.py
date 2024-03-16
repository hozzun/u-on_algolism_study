def dfs(current_node):
    global cnt
    global result

    if current_node == b:   # 찾고자 하는 사람 노드에 도착한 경우
        result.append(cnt)   # count된 촌수를 저장

    for i in graph[current_node]:   # 인접 노드 중 방문하지 않은 곳
        if visited[i] == 0:
            visited[i] = 1   # 방문표시
            cnt += 1    # cnt 증가
            dfs(i)     # 이동한 노드를 current_node로 넘겨 dfs 호출

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

visited = [0]*(n+1)
cnt = 0
result = []   # 촌수 저장하기 위한 결과 리스트 / 최종적으로 길이가 0이면 관계 x -> -1 출력

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)    # 무향 그래프
    graph[y].append(x)

visited[a] = 1
dfs(a)

if len(result) == 0:
    print(-1)
else:
    print(result[0])
