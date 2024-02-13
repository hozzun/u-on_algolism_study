T = int(input())

for tc in range(1, T+1):
    s, t = list(input().split())
    len_t = len(t)
    len_s = len(s)


    if s*len_t == t*len_s:  # 두 문자열의 크기가 같도록 만들어줌
        result = 'yes'  # 일치
    else:
        result = 'no' #불일치

    print(f'#{tc} {result}')
