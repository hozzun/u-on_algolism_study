# Python 메모리: 31120KB, 시간: 44ms

T = int(input())
arr = [[0] * 100 for _ in range(100)] # 100 x 100 도화지
answer = 0 # 최종 값
for tc in range(1, T+1):
    N, M = map(int, input().split())

    for i in range(N, N+10): # N+10 x M+10의 색종이 (10 x 10 정사각형)
        for j in range(M, M+10):
            arr[i][j] = 1 # 1 넣으면서 붙여줌

for i in range(100): # 도화지 돌면서
    for j in range(100):
        if arr[i][j] == 1: # 1이 붙어있으면
            answer += 1 # 1 증가

print(answer) # 출력
