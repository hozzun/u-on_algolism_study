# 메모리 : 59576 / 시간 : 167ms

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = [[0]*n for _ in range(n)]   # 90도씩 회전할 때마다 회전된 배열 저장
    r = [[0]*n for _ in range(n)]   # 최종 결과값 저장 배열

    import copy
    # 90도씩 회전
    print(f'#{tc}')
    for i in range(3):   # 90, 180, 270도 회전
        for j in range(n):   # 배열 순회
            s = ''
            for k in range(n):
                result[k][j] = arr[n-1-j][k]   # 회전
                s += str(arr[n-1-k][j])    # 회전된 배열의 한 행 값 3개를 str형태로 합쳐 최종 출력 배열(r)의 해당 위치에 저장.
            r[j][i] = s
        arr = copy.deepcopy(result)
    
    # 출력
    for i in range(n):
        for j in range(3):
            print(r[i][j], end = ' ')
        print()
