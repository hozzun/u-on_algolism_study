# 메모리: 60,460KB, 시간: 201ms

'''
< idea >
N x N 의 배열에서 0~N까지 하는 인덱스는 N // 2 로 보았음.
그래서 계산 쭉해서 N // 2 인덱스 기준으로 하드코딩 진행함
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)] # 입력

    answer = 0 # 최종 값
    idx = N // 2 # 중심 인덱스
    r = idx + 1 # 레인지 범위 설정 값
    c = idx # 레인지 범위 설정 값
    flag = 0 # 브레이크용
    while True:
        if flag == 1: # 브레이크용
            break
        for i in range(N): # i는 0~N까지 돌기때문에 유지
            if flag == 1: # 브레이크용
                break
            if i <= idx: # 만약 i가 N // 2보다 작거나 같다면
                r -= 1 # 범위 조절
                c += 1
            elif i > idx: # 크다면
                r += 1 # 범위 조절
                c -= 1
            for j in range(r, c): # 조절한 범위
                answer += arr[i][j] # 최종 값에 더해줌
                if i == N-1: # 만약 끝에 도달했다면
                    flag = 1 # 브레이크용
                    break

    print(f'#{tc} {answer}') # 출력
