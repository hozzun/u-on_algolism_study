# 백준 21921 번 블로그 
# 메모리 58780KB 시간 192ms 코길 440B

# -----  for 문 돌려서 했더니 안되고 자꾸 시간초과!!!!!!!! 
# ----- 고민하던 와중.. 예전에 호준오빠가 알려줬던 누적합 공식인가 뭐시기가 생각남 
# 그 방식을 이용해서 풀었음!!!!!! 

N, X = map(int, input().split())
arr = list(map(int, input().split()))
max_v = 0 # 최댓값
cnt = 0 # 최댓값 몇 개 나왔는지 카운트 해준 변수 

sum_list = [0 for _ in range(N + 1)] # 누적합 리스트 만들어줄거임.. 

for i in range(N):
    sum_list[i + 1] = sum_list[i] + arr[i] # [0, 1, 5, 7, 12, 13]

for j in range(X, N + 1):    # 누적 합의 (j번째 값 - j-X번째 값)
    cur_sum = sum_list[j] - sum_list[j - X] # [5, 6, 7, 5]
    if cur_sum > max_v:
        max_v = cur_sum
        cnt = 1
    elif cur_sum == max_v:
        cnt += 1

if max_v == 0: # max_v 0이면
    print('SAD') # 새드 ㅠㅠ~

else:
    print(max_v)
    print(cnt)


#---- 실패 버전 --- ㅠㅠ 시초 버전 .. 

N, X = map(int, input().split())
arr = list(map(int, input().split()))
max_v = 0
cnt = 0

for i in range(N - X + 1):
    val_sum = 0
    for j in range(i, i + X):
        val_sum += arr[j]
        max_v = max(val_sum, max_v)

for i in range(N - X + 1):
    val_sum = 0
    for j in range(i, i + X):
        val_sum += arr[j]
        if val_sum == max_v:
            cnt += 1

if max_v == 0:
    print('SAD')
else:
    print(max_v)
    print(cnt)
