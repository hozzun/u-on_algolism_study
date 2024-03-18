# 백준 7983번 내일할거야
n = int(input())
homework = [] 
for _ in range(n):
    d, t = tuple(map(int, input().split())) # hw 튜플 형태로 저장 
    homework.append((d, t))

homework.sort(key = lambda x : (x[1]), reverse=True) # 끝나는 일이 제일 뒤로 오게 정렬해줬음 

hw, day = homework[0][0], homework[0][1]
result = day - hw

for i in range(1, len(homework)):
    hw, day = homework[i]
    if result > day:
        result = day - hw 
    else:
        result = result - hw

print(result)
