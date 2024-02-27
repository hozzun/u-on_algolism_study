for tc in range(1, 1+int(input())):
    N = int(input())

    matrix_1 = []
    matrix_2 = []
    matrix_3 = []

    for _ in range(N):
        a = list(map(int, input().split()))
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

    # 근데 이제 어떻게 출력하지?
