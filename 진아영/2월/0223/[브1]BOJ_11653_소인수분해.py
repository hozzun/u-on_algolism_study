# 메모리 109240 KB, 시간 312 ms

N = int(input())
i = 2

while N > 1:
    if N % i == 0:     # 소인수이면
        N /= i         # N 재할당하고
        print(i)       # 프린트
    elif N % i != 0:   # 소인수가 아니면
        i += 1         # 다음 수 찾기
