# 백준 7983번 내일할거야
# 메모리 247796kb 시간 2248ms zhrlf 397
n = int(input())
homework = [] 
for _ in range(n):
    d, t = tuple(map(int, input().split())) # hw 튜플 형태로 저장 
    homework.append((d, t))

homework.sort(key = lambda x : (x[1]), reverse=True) # 끝나는 일이 제일 뒤로 오게 정렬해줬음 

hw, day = homework[0][0], homework[0][1] # hw, day 처음 초기 값 설정 
result = day - hw # result 에 day - hw / 13 - 1 =12 

for i in range(1, len(homework)): # 1부터 비교 시작 
    hw, day = homework[i] # 새로운 hw, day 값 주기 
    if result > day: # 만약에 result 가 day 보다 크다면 
        result = day - hw # result day -  hw 값 새로 갱신해줌 / 10 - 3 = 7
    else: 
        result = result - hw # 작으면 result값은 result 랑 hw 값이랑 빼줌 / 7 - 2 = 5

print(result)

# ------- 실패작 
# 처음에는 visited 이용해서 해주려 했음 미완성이지만 이렇게 하면 백퍼 시간초과 메모리 초과날듯 ~~~ 그래서 방법 바꿈 
n = int(input())
homework = [] 
for _ in range(n):
    d, t = tuple(map(int, input().split())) 
    homework.append((d, t))

homework.sort(key = lambda x : (x[1]), reverse=True) 
 
max_val = homework[0][1]
print(max_val)
visited = [0] * (max_val + 1)
# print(visited)

for i in range(len(homework)):
    hw, day = homework[i]
    for j in range(day, day - hw , -1):
        if j >= 0 and visited[j] == 0:
            visited[j] = 1
            break

print(visited)

