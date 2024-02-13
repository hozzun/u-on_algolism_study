A = int(input())
B = int(input())
C = int(input())
result = A * B * C

for i in range(10):       # 0~9까지 숫자 개수 세기
    num = 0
    for j in str(result):
        if i == int(j):
            num += 1
    print(num)
