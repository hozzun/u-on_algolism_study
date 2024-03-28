# 백준 2668번 숫자 고르기 
# 메모리 31120kb 시간 44ms 코길 497
N = int(input())
arr = [0] * (N + 1) # 일단 숫자를 1차원 배열에 넣어줌 
num = [[] for _ in range(N + 1)] # 리스트로 묶어서 넣어줌 엥 근데 한번에 가능할듯 

for i in range(1, N + 1):
    arr[i] = int(input())

for i in range(1, N + 1):
    num[i].append(arr[i])

# N = int(input())
# num = [[] for _ in range(N + 1)] # 아놔 한번에 가능이네 쩝~,, 
# for i in range(1, N + 1):
#     num[i].append(int(input()))

# print(num)
# print(arr)


# idea . 앞에서부터 방문해서 방문표시 해줌 , 방문표시가 1인데 시작 숫자랑 값이 똑같으면 시작 숫자를 리스트에 넣어줌 

result = []

def dfs(start, val):
    visited[val] = 1

    for i in num[val]:
        if visited[i] == 0: # 방문한적 없는 곳이면
            dfs(start, i) # 재귀를 계속 돈다! 
        elif visited[i] != 0 and i == start: # 만약에 방문을 했는데 i 값과 start 값이 같으면! (= 사이클이라는 것)
            result.append(i) # result 에 추가! 

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    dfs(i, i)


print(len(result))
for i in result:
    print(i)
