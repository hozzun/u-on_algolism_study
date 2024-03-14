# 백준 2644번 촌수계산
# 메모리 31120kb 시간 40ms 코드길이 501b

# 밑에 global cnt 로 줬는데 왜 이렇게 하면 틀릴까???????
# ---------- 실패작 ---------
n = int(input())
person1, person2 = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0
result = -1
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


def dfs(i, j):
    global cnt
    global result

    if i == j:
        result = cnt
        return

    visited[i] = 1
    for w in arr[i]:
        if visited[w] == 0:
            cnt += 1
            dfs(w, j)
            cnt -= 1 # 헐 !! 현조오빠가 도와줌 !!!!  만약에 잘못된 루트로 갔으면 다시 돌아와줘야 해서 cnt 를 -1 해줘야함 
    return


dfs(person1, person2)
print(result)

# --------- 성공 ----------
n = int(input())
person1, person2 = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
result = -1
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


def dfs(i, j, cnt):
    global result

    if i == j:
        result = cnt
        return

    visited[i] = 1
    for w in arr[i]:
        if visited[w] == 0:
            dfs(w, j, cnt + 1)
    return


dfs(person1, person2, 0)
print(result)
