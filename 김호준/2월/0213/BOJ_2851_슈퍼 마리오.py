arr = [] # 점수 리스트
for tc in range(10):
    score = int(input())
    arr.append(score) # 점수 넣기

cnt = 0 # 100까지 점수 기록용
temp = 0 # 100 넘어가면 기록용
for i in arr:
    if cnt + i <= 100: # cnt와 i의 합이 100 이하라면
        cnt += i # 계속 더해줌
        if cnt == 100: # 만약 100이 되면 
            break # 브레이크
    elif cnt + i > 100: # cnt랑 i의 합이 이상이 된다면
        temp += i # 템프에 따로 저장
        break

a = 100 - cnt # 100 - 100이전까지의 합
b = (cnt + temp) - 100 # 100넘어서의 합 - 100
if cnt == 100: # 그냥 cnt가 100이면
    print(100) # 100 출력
elif a < b: # 100 이전까지의 합이 더 작으면
    print(cnt) # 출력
elif a > b: # 100 넘어서까지의 합이 더 작으면
    print(cnt+temp) # 출력
elif a == b: # 같으면
    print(cnt+temp) # 큰값 출력
