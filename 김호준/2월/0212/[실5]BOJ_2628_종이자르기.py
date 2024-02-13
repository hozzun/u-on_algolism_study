G, S = map(int, input().split())
T = int(input())

G_arr = [0, G] # 가로 그룹 [0, 10, 4]
S_arr = [0, S] # 세로 그룹 [0, 8, 3, 2]
for _ in range(T):
    N, M = map(int, input().split())
    if N == 1: # 여기서 반대로 했다가 애먹음
        G_arr.append(M) # 앞에 1이면 세로로 자르니까 가로길이 나눠짐
    else:
        S_arr.append(M) # 0이면 가로로 자름 세로길이 나눠짐

G_arr.sort() # 정렬시켜줌 [0, 4, 10]
S_arr.sort() # [0, 2, 3, 8]

G_result = 0 # 가로 최대값
for i in range(len(G_arr)-1):
    if G_result < G_arr[i+1] - G_arr[i]: # 뒤에꺼에서 앞에꺼 뺌
        G_result = G_arr[i+1] - G_arr[i] # 그럼 길이 나옴
        
S_result = 0 # 세로 최대값
for j in range(len(S_arr)-1):
    if S_result < S_arr[j+1] - S_arr[j]:
        S_result = S_arr[j+1] - S_arr[j]

print(G_result * S_result)
