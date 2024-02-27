# 메모리: 58,528KB, 시간: 152ms

# 처음에 90도 등등 회전시키는게 뭔소린가 해서 규칙 찾다가 화남~
def recur(arr): # (90도 회전 함수)
    result = [[0] * N for _ in range(N)] # 계속 회전시켜줄 배열만듦
    for i in range(N):
        for j in range(N):
            result[i][j] = arr[N-1-j][i] # 규칙찾고 계산하는데 현타오더라 이게 왜 D2인거임;
    return result # 만든 배열 내보냄 (90도 회전)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _  in range(N)]

    # 90도 회전
    tornado90 = recur(arr)
    # 180도 회전
    tornado180 = recur(tornado90)
    # 270도 회전
    tornado270 = recur(tornado180)

    print(f'#{tc}')
    for a, b, c in zip(tornado90, tornado180, tornado270): # 각 배열 합쳐줌
        '''
        zip함수로 예를들어 
        7 4 1 
        8 5 2 
        9 6 3 이렇게 3 x 3 배열형태로 있으면
        --> 741
            852
            963 으로 붙혀서 하나로 만들어줌
        '''
        aa = ''.join(a) # 이거(출력형식) 하느라 또 애먹음 아오 화나
        bb = ''.join(b)
        cc = ''.join(c)
        print(aa, bb, cc)
