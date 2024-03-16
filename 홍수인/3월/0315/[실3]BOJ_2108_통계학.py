n = int(input())
num_lst = [int(input()) for _ in range(n)]

# 1. 산술평균
print(int(sum(num_lst)/n))

# 2. 중앙 값
num_lst.sort()
print(num_lst[n//2])

# 3. 최빈 값
set_lst = set(num_lst)
count_lst = []   # 숫자의 갯수를 저장할 리스트

if len(set_lst) == n:  # 모든 수가 중복되지 않는 경우
    if len(num_lst) == 1:
        print(num_lst[0])
    else:
        print(num_lst[1])
else:
    for i in num_lst:
        a = num_lst.count(i)
        if a in count_lst:    # 개수가 똑같은 게 존재하면
            result = i
        count_lst.append(a)

    max_val = 0
    set_l = list(set_lst)
    set_l.sort()
    if max(count_lst) == result:  # 개수가 같은 count수가 최대 count이면 i는 최빈값이 여러개인 리스트 중 두번쨰 작은수가 됨.
        print(i)
    else:   # 겹치는 count의 수가 최빈값의 갯수가 아닌경우 최대 count 값을 찾아 최빈값 구함.
        for i in range(len(count_lst)):
            if count_lst[i] > max_val:
                max_val = count_lst[i]
                idx = i
        print(set_l[idx])

# 4. 범위
print(num_lst[-1] - num_lst[0])
