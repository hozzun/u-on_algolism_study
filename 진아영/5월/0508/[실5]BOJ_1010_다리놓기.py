# 파이썬 31120 KB, 76 ms

for tc in range(int(input())):

    N, M = sorted(map(int, input().split()))

    one = two = three = 1

    # NCM = M! / (N! * (M-N)!)  : 조합 수 공식

    for i in range(1, M+1):
        one *= i

    for j in range(1, N+1):
        two *= j

    for k in range(1, M-N+1):
        three *= k

    print(one // two // three)
