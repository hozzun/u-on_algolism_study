A = int(input())
B = int(input())
C = int(input())

x = A*B*C
strx = str(x)

for i in range(10): # 0부터 9까지
    count=0
    for number in strx:  # strx에 0부터 9까지의 숫자가 각 몇개 있는지 count해서 출력
        n=int(number)
        if i == n :
            count += 1
    print(count)
