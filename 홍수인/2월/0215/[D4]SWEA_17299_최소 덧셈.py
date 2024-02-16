T = int(input())

for tc in range(1, T+1):
    a = input()
    num_lst = [i for i in a]
    min_val = int(a)

    for i in range(1, len(a)):  # 경우의 수
        x = y = ''
        for j in range(i):  # x구하기 ( 수 분할 )
            x += num_lst[j]
        for k in range(i, len(a)):  # y 구하기
            y += num_lst[k]
        sum_val = int(x) + int(y)

        if sum_val < min_val:   # 합의 최소값 구하기
            min_val = sum_val

    print(f'{tc} {min_val}')
