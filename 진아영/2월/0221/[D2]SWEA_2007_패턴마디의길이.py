for tc in range(1, 1+int(input())):
    pattern = input()
    result = 0

    for i in range(1, 11):
        # 마디의 길이가 1이니까 1부터 10까지 잘라보면서 같은 문자열이면 break
        if pattern[0:i] == pattern[i+1:2*i+1]:
            result = i+1
            break

    print(f'#{tc} {result}')
