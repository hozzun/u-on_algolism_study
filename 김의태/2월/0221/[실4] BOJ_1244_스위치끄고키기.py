swich_num = int(input())
swich = list(map(int, input().split()))
st_num = int(input())
arr = [list(map(int, input().split())) for _ in range(st_num)]

for i in range(st_num):
    s = arr[i][0]
    n = arr[i][1]
    if s == 1:
        k = 1
        while n * k <= swich_num:
            if swich[n*k-1]:
                swich[n * k - 1] = 0
            else:
                swich[n * k - 1] = 1
            k += 1
    else:
        x = 0
        y = 0
        while (0 <= n-1-x) and (n-1+x+1 <= swich_num):

            for q in range(len(swich[(n - 1) - x:(n - 1) + x + 1])//2):
                if swich[(n - 1) - x:(n - 1) + x + 1][q] != swich[(n - 1) - x:(n - 1) + x + 1][-1-q]:
                    break
            else:
                y = x

            x += 1

        for v in range(y+1):
            if v == 0:
                if swich[n - 1] == 1:
                    swich[n - 1] = 0
                else:
                    swich[n - 1] = 1
            else:
                if swich[(n - 1) - v] == 1:
                    swich[(n - 1) - v] = 0
                else:
                    swich[(n - 1) - v] = 1

                if swich[(n - 1) + v] == 1:
                    swich[(n - 1) + v] = 0
                else:
                    swich[(n - 1) + v] = 1

for u in range(swich_num):
    if u > 0 and u % 20 == 0:
        print(end = '\n')
    else:
        print(swich[u], end = ' ')
