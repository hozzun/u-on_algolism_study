T = int(input())

for tc in range(1, T+1):
    a = input()
    num_lst = [i for i in a]  # 입력받은 수 한자리씩 lst에 저장

    for i in range(2, 10):   # input 배수의 list와 input list 같은지 판별
        new_n = str(int(a) * i)
        new_num = [j for j in new_n]

        if sorted(new_num) == sorted(num_lst):
            result = 'possible'
            break
        else:
            result = 'impossible'

    print(f'#{tc} {result}')
