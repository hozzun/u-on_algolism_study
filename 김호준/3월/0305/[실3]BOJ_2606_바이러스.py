# Python 메모리: 31120KB, 시간: 48ms, 코드길이: 455

def recur(x):
    if not graph[x]: # 그래프 x인덱스 안에 아무것도 없으면
        return # 뒤로

    for i in graph[x]: # 그래프 안에 값 돌면서
        if visited[i] == 0: # 방문 안했으면
            visited[i] = 1 # 방문 처리
            recur(i) # i인덱스 그래프로 다시 dfs


N = int(input())
graph = [[] for _ in range(N+1)] # 그래프
visited = [0 for _ in range(N+1)] # 방문처리

T = int(input())
for tc in range(1, T + 1):
    c1, c2 = map(int, input().split())

    graph[c1].append(c2) # 양방향
    graph[c2].append(c1)

recur(1) # 함수 발동

cnt = 0
for i in visited[2:]: # 2번째 부터 돌면서 1이 있으면 횟수 1씩 증가
    if i == 1:
        cnt += 1

print(cnt) # 출력
