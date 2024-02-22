# 메모리: 43,794KB, 시간: 103ms

a = [1, 3, 5, 7, 8, 10, 12] # 31일 월만 리스트 따로 만듦
T = int(input())
for tc in range(1, T+1):
    arr = input()

    if int(arr[4:6]) >= 1 and int(arr[4:6]) < 13: # 월 계산
        if int(arr[4:6]) == 2: # 2월 따로 빼주고
            if int(arr[6:8]) >= 1 and int(arr[6:8]) < 29:
                print(f'#{tc} {arr[0:4]}/{arr[4:6]}/{arr[6:8]}')
            else:
                print(f'#{tc} -1')
        elif int(arr[4:6]) in a: # 31일 월
            if int(arr[6:8]) >= 1 and int(arr[6:8]) < 32:
                print(f'#{tc} {arr[0:4]}/{arr[4:6]}/{arr[6:8]}')
            else:
                print(f'#{tc} -1')
        else: # 나머지
            if int(arr[6:8]) >= 1 and int(arr[6:8]) < 31:
                print(f'#{tc} {arr[0:4]}/{arr[4:6]}/{arr[6:8]}')
            else:
                print(f'#{tc} -1')
    else: # 월 1~12월 안에 안들면 다 아웃
        print(f'#{tc} -1')
