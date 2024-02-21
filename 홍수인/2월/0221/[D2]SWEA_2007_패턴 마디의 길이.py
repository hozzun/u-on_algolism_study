# 메모리 43520 시간 115

T = int(input())
for tc in range(1, T+1):
    s = input()
    w = s[0:2]

    for i in range(1, 29):
        if s[i:i+2] == w:   # w와 같은 구간이 있다면 그 전 idx를 저장.
            idx = i-1       # 0부터 idx까지가 패턴의 길이
            break
        else:
            continue

    print(f'#{tc} {idx+1}')
