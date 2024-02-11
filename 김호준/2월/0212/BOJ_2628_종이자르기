G, S = map(int, input().split())
T = int(input())

G_arr = [0, G]
S_arr = [0, S]
for _ in range(T):
    N, M = map(int, input().split())
    if N == 1:
        G_arr.append(M)
    else:
        S_arr.append(M)

G_arr.sort()
S_arr.sort()

G_result = 0
for i in range(len(G_arr)-1):
    if G_result < G_arr[i+1] - G_arr[i]:
        G_result = G_arr[i+1] - G_arr[i]
        
S_result = 0
for j in range(len(S_arr)-1):
    if S_result < S_arr[j+1] - S_arr[j]:
        S_result = S_arr[j+1] - S_arr[j]

print(G_result * S_result)
