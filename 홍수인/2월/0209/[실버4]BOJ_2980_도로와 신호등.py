N, L = list(map(int, input().split()))

result = pre_D = 0   # 이동하는데 걸리는 시간 총 합
for i in range(N):
    D, R, G = list(map(int, input().split()))
    
    result += D - pre_D
    if result % (R + G) < R:  # 빨간불일 경우
        result += R-(result % (R + G))
    else: # 초록불일 경우
        pass
    
    pre_D = D

result += L - D  # 마지막 신호등 ~ 종점
print(result)
