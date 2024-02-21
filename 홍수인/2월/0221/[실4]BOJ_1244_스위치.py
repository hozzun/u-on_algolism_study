# 메모리 108080 시간 112ms

N = int(input())
status = list(map(int, input().split()))
N_student = int(input())

for i in range(N_student):
    arr = list(map(int, input().split()))
    sw_num = arr[1]

    if arr[0] == 1:   # 남학생일 경우
        for i in range(1, N//arr[1]+1):   # 배수의 개수만큼 반복
            if status[i*sw_num-1] == 0:
                status[i*sw_num-1] = 1
            else:
                status[i*sw_num-1] = 0

    else:    # 여학생일 경우
        cnt = 0
        for i in range(1, arr[1]):
            try:
                if status[sw_num-1-i] == status[sw_num-1+i]:
                    cnt += 1
                else:
                    break
            except IndexError:
                break

        for j in range(0, cnt+1):
            if status[sw_num-1-j] == 0:
                status[sw_num-1-j] = 1
                status[sw_num-1+j] = 1
            else:
                status[sw_num-1-j] = 0
                status[sw_num-1+j] = 0

for out in range(1, N+1):
    print(status[out-1], end=' ')
    if out % 20 == 0:
        print()
