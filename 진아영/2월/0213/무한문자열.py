for tc in range(1, 1 + int(input())):
 
    s, t = list(map(str, input().split()))
    result = 'yes'
 
    n = len(s) * len(t)         # 최소공배수 찾기 -> 못찾음 ㅠㅠ 걍 곱하기로..
 
    for i in range(n):
        if s[i % len(s) - 1] != t[i % len(t) - 1]:     # 공통 문자열 순서 맞는지 확인
            result = 'no'
            break
 
    print(f'#{tc} {result}')
