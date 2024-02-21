# 백준 8979번 올림픽 메모리 31120 KB 시간 84ms 
# idea 는 금메달 비교해서 제일 많은 나라 1등 
# 만약 금메달이 같다면 은메달 비교해서 많은 나라 +1
# 만약 은메달도 같다 -> 동메달 비교해서 많은 나라 +1
# 만약 동메달도 같다 -> 공동 순위, , 
# 근데 쫌 모르겠어서 ㅎㅎ... 나라 따로 빼서 저장하는거 다른 사람꺼 쫌 참고했어.. sorry ㅎ ㅎ 

N, K = list(map(int,input().split()))
rank = [] # 비교해줄 나라들 모아놓기 
for i in range(N):
    arr = list(map(int, input().split()))
    if arr[0] != K: # 만약 arr[0]이 K가 아닐 때 
        rank.append(arr) # arr를 rank에 추가  
    else:
        pick = arr # pick은 내가 궁금한 K번째 나라 뺴놓은거 

# print(rank)
# print(pick)

grade = 1 
for i in range(len(rank)):
    if rank[i][1] > pick[1]: # 만약에 rank의 i번째의 금메달이 K번째 금메달 보다 많으면 
        grade  += 1 # 나보다 앞 등수 이므로 grade += 1
    
    elif rank[i][1] == pick[1]: # 만약에 금메달 수가 똑같다면 
        if rank[i][2] > pick[2]: # 은메달을 비교 
            grade += 1 # 은메달이 나보다 더 많다면 grade += 1
        
        elif rank[i][2] == pick[2]: # 은메달 수가 똑같으면 
            if rank[i][3] > pick[3]: # 동메달 수 비교해서 
                grade  += 1 # 동메달도 나보다 더 많으면 grade += 1

print(grade) # 등수 출력 
