# 백트래킹 하다가 시간초과 에바라 호준오빠가 준 힌트로 도전~~
# 근데 뭐가 틀린거지~~~? 근데 so sleepy~~~ 그럼 이만~~~ 낼 보자구~~~~~


def dfs(j):
    global i, cur_arr, result_arr
    next = arr[j]  # 다음 검사할 수

    if not visited[next]:
        visited[next] = 1
        cur_arr.append(arr[next])
        dfs(next)
    else:
        if i == arr[next]:
            result_arr.extend(cur_arr)
            return
        

N = int(input())
arr = [0]

for _ in range(N):
    arr.append(int(input()))

result_arr = []

for i in range(1, N+1):
    visited = [0] * (N+1)
    visited[arr[i]] = 1
    cur_arr = [arr[i]]
    dfs(i)

result_arr.sort()
print(len(result_arr))
for k in result_arr:
    print(k)
