import copy

def dfs(k):
    global line, adjl, visited
    
    lst = adjl[k]
    
    for l in lst:
        if not visited[l]:
            visited[l] = 1
            line += 1
            dfs(l)

def solution(n, wires):
    global line, visited, adjl
    answer = 100

    
    for i in range(n-1):    # 간선 하나씩 없애보면서 완전탐색
        new_wires = copy.deepcopy(wires)
        new_wires.pop(i)
        visited = [0] * (n+1)
        adjl = [[] for _ in range(n+1)]
        for w in range(n-2):
            a, b = new_wires[w]
            adjl[a].append(b)
            adjl[b].append(a)

        result = []               # 전력망 길이(2개)가 들어갈 리스트
        for j in range(1, n+1):   # 한 간선을 없앴을때 이때의 전력망 구하기
            if not visited[j]:
                line = 1
                visited[j] = 1
                dfs(j)
                result.append(line)

        if len(result) > 1:
            answer = min(answer, abs(result[0]-result[1]))
    
    return answer
