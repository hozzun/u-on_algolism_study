# 58,244 kb, 153 ms

for tc in range(1, 1+int(input())):

    len_1, len_2 = map(int, input().split())
 
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    max_sum = -999999999999
 
    # 뭐가 더 짧은지?
    if len_1 <= len_2:
        for i in range(len_2 - len_1 + 1):
            lst = arr_2[i : i + len_1]
            cur_sum = 0
            for a in range(len_1):
                cur_sum += lst[a] * arr_1[a]
            if cur_sum > max_sum:
                max_sum = cur_sum
 
    else:
        for i in range(len_1 - len_2 + 1):
            lst = arr_1[i: i + len_2]
            cur_sum = 0
            for a in range(len_2):
                cur_sum += lst[a] * arr_2[a]
            if cur_sum > max_sum:
                max_sum = cur_sum
 
    print(f'#{tc} {max_sum}')
