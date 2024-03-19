# 백준 14888번 연산자 끼워넣기 
# 메모리 31120kb 시간 56ms 코길 887b

def dfs(plus, minus, mul, div, i, val):
    global min_val, max_val

    if i == N: # 사실 처음에 N-1 로 했는데 바꿈 ㅎ..
        min_val = min(val , min_val)
        max_val = max(val, max_val)
        return 

    else:
        if plus > 0:
            dfs(plus - 1, minus, mul, div, i + 1, val + arr[i])
        if minus > 0:
            dfs(plus, minus -1 , mul, div, i + 1, val - arr[i])
        if mul > 0:
            dfs(plus, minus, mul -1 , div, i + 1, val * arr[i])
        if div > 0: # 처음에 그냥 나누기만 했다가 조건있는거 뒤늦게 봄@!@@@
            if val < 0:
                dfs(plus, minus, mul, div - 1, i + 1, -(-val // arr[i])) # 아놔!!!!!! 여기서 div-1 안해줘서 자꾸 틀린거였음!!!!!! 
            else:
                dfs(plus, minus, mul, div -1 , i + 1, val // arr[i])

N = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))
min_val = 1e9
max_val = -1e9
dfs(op[0], op[1], op[2], op[3], 1, arr[0])
print(max_val)
print(min_val)

# ------------- 실패작 -----------------

def dfs(plus, minus, mul, div, i, val):
    global min_val, max_val

    if i == N-1:
        min_val = min(min_val, val)
        max_val = max(max_val, val)
        return 

    else:
        if plus > 0:
            dfs(plus - 1, minus, mul, div, i + 1, val + arr[i + 1])
        if minus > 0:
            dfs(plus, minus -1 , mul, div, i + 1, val - arr[i + 1])
        if mul > 0:
            dfs(plus, minus, mul -1 , div, i + 1, val * arr[i + 1])
        if div > 0:
            if val < 0:
                dfs(plus, minus, mul, div - 1 , i + 1, -(-val // arr[i + 1]))
            else:
                dfs(plus, minus, mul, div -1 , i + 1, val // arr[i + 1])

N = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))
min_val = 1e9
max_val = -1e9
val = arr[0]
dfs(op[0], op[1], op[2], op[3], 0, val)
print(max_val)
print(min_val)
