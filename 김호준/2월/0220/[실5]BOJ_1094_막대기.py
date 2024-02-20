# Python 메모리: 31252KB, 시간: 44ms

X = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]

count = 0
for i in range(len(stick)):
    if X >= stick[i]: # X가 숫자도는거보다 크면
        count += 1 # 횟수 1 증가
        X -= stick[i] # 빼주셈
        if X == 0: # X가 0이 되면
            break # 종료
    else: # 나머지는
        pass # 패스~

print(count)
