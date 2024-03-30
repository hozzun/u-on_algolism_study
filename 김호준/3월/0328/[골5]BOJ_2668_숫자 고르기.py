# Python 메모리: 31120KB, 시간: 44ms, 코드 길이: 493B
# 처음에 1-3, 3-1 이렇게 같은거만 찾다가 실패하고 그림그려보다가 트리같아서 풀어봄

def dfs(idx, node): # 1번 index, 우리가 찾을 node 값
    global result
    visited[idx] = True

    for i in graph[idx]:
        if not visited[i]:
            dfs(i, node) # idx에 연결되어 있는 node로 계속 들어가기
        elif visited[i] and i == node: # 만약 연결된 노드에 방문했었고, 우리가 찾는 값이면 리스트에 추가
            result.append(i)

# [1]:[2, 3], [2]:[], [3]:[1], [4]:[6], [5]:[4, 5], [6]:[7], [7]:[]
N = int(input())

graph = [[] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    # 문제 그림처럼 3의 1 넣고, 1의 2 넣고, 1의 3에 넣고 넣어주면 위에처럼 트리됨
    graph[int(input())].append(i)

result = []
for i in range(1, N+1):
    visited = [False] * (N + 1) # 1~N까지 다 뒤져봐야하니 방문처리 매번 리셋
    dfs(i, i) # 1, 1부터 시작

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])
