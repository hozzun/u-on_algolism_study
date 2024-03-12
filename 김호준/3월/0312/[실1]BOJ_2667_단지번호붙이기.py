# Python 메모리: 31196KB, 시간: 60ms, 코드 길이: 939B

import sys
sys.setrecursionlimit(10**6)

di = [1, 0, -1, 0] # 상 하 좌 우
dj = [0, 1, 0, -1]

def dfs(y, x): # dfs로 돌면서 visited에 1, 2, 3 이런식으로 바꿔줌
    # 첫 번째 1 순회할 때는 1로, 두번 째 1 순회할 때는 2 이런식으로
    # 문제에서 주어진 사진과 같이
    global cnt
    visited[y][x] = cnt

    for k in range(4):
        ni = y + di[k]
        nj = x + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if graph[ni][nj] > 0 and not visited[ni][nj]:
                dfs(ni, nj)


N = int(input())

graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

answer = 0
cnt = 1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            answer += 1 # 단지
            cnt += 1 # 그림과 같이 visited에 1, 2, 3 넣기 위한 용도

result = []
count = 1
while True:
    if count == cnt: # 종료 조건
        break

    ans = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == count:
                ans += 1

    result.append(ans) # 1, 2, 3 세어주고 리스트 안에 넣음 각각
    count += 1 # 1 -> 2 -> 3 탐색용도

result.sort() # 정렬

# 출력
print(answer)
for i in range(len(result)):
    print(result[i])
