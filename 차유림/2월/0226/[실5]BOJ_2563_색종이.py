# 실패작 ~~~,,,, 0이 나옴 ㅜㅜ 
# N = int(input())
# arr = [[0] * 100 for _ in range(100)]
# for i in range(N):
#     r, c = map(int, input().split())
#     r1, c1, r2, c2 = r, c+10, r+10, c
#     for k in range(r1, r2 + 1):
#         for l in range(c1, c2 + 1):
#             if arr[k][l] > 0 :
#                 arr[k][l] += 1
#             else:
#                 arr[k][l] = 1
    
# cnt = 0
# for ra in range(100):
#     for ca in range(100):
#         if arr[ra][ca] == 1 or arr[ra][ca] == 2 or arr[ra][ca] == 3: 
# 앗 생각해보니까 색종이 더 여러장이면 4도 있고 5일수도 있고 그럴듯...헷 실수~~ 
#             cnt += 1    

# print(cnt) 

# ----------------------------------------------------
# 백준 2563번 색종이 메모리 31120kb 시간 44ms
N = int(input())
arr = [[0] * 100 for _ in range(100)] # 도화지 만들기
for i in range(N):
    r, c = map(int, input().split()) # r,c 받기
    for k in range(r, r+10): # r,c 받은거에서 색종이 범위는 r, r+10 / c, c+10(길이가 10임)
        for l in range(c, c+10): 
            arr[k][l] += 1 # 색종이의 범위만큼 도화지에 1을 더해준다
    
cnt = 0
for ra in range(100):
    for ca in range(100):
        if arr[ra][ca] >= 1: # 1보다 클 떄만 카운트 
            cnt += 1    

print(cnt) 
