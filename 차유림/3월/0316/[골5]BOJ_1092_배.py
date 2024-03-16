# 백준 1092번 배 
# 메모리 110648KB 시간 4416ms 코길 613b

N = int(input())
limit = list(map(int, input().split()))
M = int(input())
weight = list(map(int, input().split()))

limit.sort(reverse=True)
weight.sort(reverse=True)

minute = 0

if max(weight) > max(limit):
    print(-1)

else:
    while weight:
        for i in range(N):
            for j in range(len(weight)): # weight는 계속 변동되므로 len해준다
                if weight[j] <= limit[i]:
                    weight.remove(weight[j])
                    break   
                else:
                    j += 1
                    continue   
     
        minute += 1
        
    print(minute)
