# 백준 1764번 듣보잡
# 파이파이 메모리 129872 시간 264 코길 517
# 파이썬 메모리 43920 시간 3724 (시간 실화...? )

N, M = map(int, input().split())
dbj = {} # 듣보잡 딕셔너리 만들기 
for i in range(N):
    nolisten = str(input()) # 듣지 못한 사람 딕셔너리에 추가해줌 
    if nolisten in dbj:
        dbj[nolisten] += 1
    else:
        dbj[nolisten] = 1

for j in range(M):
    nolook = str(input()) # 보지 못한 사람 딕셔너리에 추가해줌 
    if nolook in dbj:
        dbj[nolook] += 1
    else:
        dbj[nolook] = 1

dbj_cnt = 0 # 듣보잡 카운트 변수 
dbj_list = [] # 듣보잡 리스트 

for key, val in dbj.items(): # key, val 뽑기 
    if val == 2: # val 이 2인 것이 듣보잡이므로 
        dbj_cnt += 1 # 카운트 += 1 해주고 
        dbj_list.append(key) # 리스트에도 추가 

print(dbj_cnt)
dbj_list.sort() # 정렬하고 뽑아줌
for i in dbj_list:
    print(i)
