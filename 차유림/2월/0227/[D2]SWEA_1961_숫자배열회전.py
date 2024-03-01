# 출력형식 왜 나는 붙여서 안돼 리스트로 해서 그런가 ㅠ 흑ㅎ긓긓그흑 심지어 걍 냅다 제출했더니 10개 중 2개 맞았대  ㅜㅜ ㅋㅋㅋㅋㅋㅋㅋㅋ
# 실패작
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mat_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            mat_90[j][N - i - 1] = arr[i][j]

    mat_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            mat_180[N - i - 1][N - j - 1] = arr[i][j] # 원래 mat_90[i][j] 했는데 이상하게 나옴 ㅠ,, 그림 그렸을 떈 저랬는데 머지
        
    mat_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            mat_270[N - j - 1][i] = arr[i][j] # 원래 mat_180[i][j] 했는데 이상하게 나옴 ㅠ,, 바꿨더니 제대로 나옴

    print(f"#{tc}")

    # 스트링으로 바꿔줄럤는데 괄호랑 콤마 때문에 안돼 ㅜ

    for x, y, z in zip(mat_90, mat_180, mat_270):
        a = ' '.join(map(str, x))
        b = ' '.join(map(str, y))
        c = ' '.join(map(str, z))
    
        print(a, b, c)



# 성공
# swea 1961번 숫자 배열 회전 메모리 58,252kb 시간 162ms
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mat_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            mat_90[j][N - i - 1] = arr[i][j] 

    mat_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            mat_180[j][N - i - 1] = mat_90[i][j] 
        
    mat_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            mat_270[j][N - i - 1] = mat_180[i][j]

    print(f"#{tc}")

    for x, y, z in zip(mat_90, mat_180, mat_270):
        a = ''.join(map(str, x))
        b = ''.join(map(str, y))
        c = ''.join(map(str, z))
    
        print(a, b, c)
