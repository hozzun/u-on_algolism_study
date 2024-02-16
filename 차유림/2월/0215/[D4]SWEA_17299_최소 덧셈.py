T = int(input())
for tc in range(1, T+1):
    num = str(input())
    min_val = 999999
    sum_val = 0
    for i in range(1, len(num)):
        a = num[:i]
        b = num[i:len(num)]
        sum_val = int(a) + int(b)
        if min_val > sum_val:
            min_val = sum_val
 
    print(f"#{tc} {min_val}")
