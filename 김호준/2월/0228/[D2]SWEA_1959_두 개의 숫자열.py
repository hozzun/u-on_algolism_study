# 메모리: 45,060KB, 시간: 112ms

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if N <= M: # N이 M보다 작거나 같을 때
        answer = 0 # 최종 값
        s = 0 # 범위 늘리기 용
        for i in range(M-N+1): # 반복 횟수
            cnt = 0
            for j in range(N): # N번 돌면서
                cnt += arr1[j] * arr2[j+s] # cnt에 넣어줌
            s += 1 # 다음 범위로
            '''
            규칙이 인데스 번호로 보면 N = 3, M = 5일 때
            0 * 0 / 1 * 1 / 2 * 2
            0 * 1 / 1 * 2 / 2 * 3
            0 * 2 / 1 * 3 / 2 * 4
            총 M-N+1번 동안
            왼쪽은 0~N만큼 오른쪽은 1씩 증가하며 반복함
            '''

            answer = max(answer, cnt) # 큰 값 저장

        print(f'#{tc}', answer)

    # N이 더 클 때
    elif N > M:
        answer = 0
        s = 0
        for i in range(N-M+1):
            cnt = 0
            for j in range(M):
                cnt += arr2[j] * arr1[j+s]
            s += 1

            answer = max(answer, cnt)

        print(f'#{tc}', answer)
