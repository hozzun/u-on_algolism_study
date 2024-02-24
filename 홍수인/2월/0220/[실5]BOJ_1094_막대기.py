# 메모리 108080 / 시간 112ms

x = int(input())
stick = stick_l = 64
stick_lst = [64, 32, 16, 8, 4, 2, 1]

stick_l = 0
cnt = 0

while stick_l != x:  # 자른 막대기들의 합인 stick_l의 길이가 x가 될 때까지 반복
    if stick_lst[0] > x:   # x보다 큰 경우 삭제
        stick_lst.pop(0)
    elif stick_lst[0] == x:   # x와 같은 경우 1이 출력되도록
        cnt = 1
        break
    else:   # x보다 작은 경우
        if stick_l + stick_lst[0] <= x:   # 막대기의 합 + 0번 인덱스 -> x보다 작다면 누적합, cnt += 1
            stick_l += stick_lst[0]
            cnt += 1
        else:
            stick_lst.pop(0)   # 막대기의 합 + 0번 인덱스 -> x초과할 경우 지움
print(cnt)
