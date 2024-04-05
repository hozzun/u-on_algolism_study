def dfs(start, graph, visited):
    global cnt
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, graph, visited)
            cnt += 1
    return cnt


def solution(n, wires):
    global cnt
    answer = 1e9
    graph = [[] for _ in range(n+1)]
    for start, end in wires:
        graph[start].append(end)
        graph[end].append(start)
    
    for start, end in wires:
        cnt = 1
        visited = [False] * (n+1)
        visited[end] = True
        count = dfs(start, graph, visited)
        answer = min(answer, abs(n - count), count)
    
    return answer
