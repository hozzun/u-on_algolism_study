T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    hour = arr[0] + arr[2]
    if arr[1] + arr[3] >= 60:  # 분의 합이 60 이상이면 시간 +1
        hour += 1
        minute = arr[1] + arr[3] - 60
    else:
        minute = arr[1] + arr[3]

    # 시간이 12 이상인 경우 -12
    if hour > 12:
        hour -= 12
    
    print(f'#{tc} {hour} {minute}')
