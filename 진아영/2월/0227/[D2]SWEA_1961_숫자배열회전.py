for tc in range(1, 1+int(input())):
    N = int(input())

    matrix_1 = []
    matrix_2 = []
    matrix_3 = []

    for _ in range(N):
        a = list(map(str, input().split()))
        matrix_1 += a
        matrix_2 += a
        matrix_3 += a

    new_matrix_1 = [[0] * N for _ in range(N)]
    new_matrix_2 = [[0] * N for _ in range(N)]
    new_matrix_3 = [[0] * N for _ in range(N)]

    for i in range(N-1, -1, -1):   # 거꾸로
        for j in range(N):         # 똑바로
            new_matrix_1[j][i] = matrix_1.pop(0)

    for i in range(N-1, -1, -1):       # 거꾸로
        for j in range(N-1, -1, -1):   # 거꾸로
            new_matrix_2[i][j] = matrix_2.pop(0)

    for i in range(N):                 # 똑바로
        for j in range(N-1, -1, -1):   # 거꾸로
            new_matrix_3[j][i] = matrix_3.pop(0)

    print(f'#{tc}')
    for a, b, c in zip(new_matrix_1, new_matrix_2, new_matrix_3):
        aa = ''.join(a)
        bb = ''.join(b)
        cc = ''.join(c)
        print(aa, bb, cc)

    '''
    1)
    zip함수로 예를들어 
    7 4 1 
    8 5 2 
    9 6 3 이렇게 3 x 3 배열형태로 있으면
    --> 741
        852
        963 으로 붙혀서 하나로 만들어줌
        
    2) 
    zip함수는 str만 되서 map(int 부분 str로 바꿈
    '''
