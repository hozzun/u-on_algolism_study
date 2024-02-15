T = int(input())
for tc in range(1, T+1):
    S = input()

    min_v = 9999999 # 최소값 초기값 설정
    for i in range(len(S)-1): # 문자열 길이에서 1뺀만큼 돌면서
        result = int(S[:i+1]) + int(S[i+1:]) # 앞에꺼 + 뒤에꺼
        if min_v > result: # 이것들로 최소값 뽑아냄
            min_v = result

    print(f'#{tc}', min_v)
