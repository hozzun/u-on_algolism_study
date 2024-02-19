for i in range(1, 1 + int(input())):

    first_H, first_M, second_H, second_M = list(map(int, input().split()))

    # 두 수의 시와 분을 각각 더해주기
    hour = first_H + second_H
    minute = first_M + second_M

    hour += (minute // 60) # 분을 60으로 나눈 몫을 시에 더해주고
    minute %= 60           # 그 나머지를 그대로 둔다 -> 분 완성!
    
    hour %= 12  # 그리고 시를 12으로 나눈 나머지로 바꾼다. -> 시 완성!
    if hour == 0:
        hour = 12  # 근데 12시일때 0시로 나와서 다시 바꿔줌 !! 이거 우째

    print(f'#{i} {hour} {minute}')
