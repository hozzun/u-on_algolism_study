N = int(input())   # 스위치 개수
switch = list(map(int, input().split()))
S = int(input())   # 학생 수

for _ in range(S):
    s, number = list(map(int, input().split()))

    # 남학생일 경우
    if s == 1:
        # 스위치를 돌면서 조건에 맞으면 스위치 켜고 끄기
        for i in range(N):
            if (i+1) % number == 0:
                if switch[i] == 0:
                    switch[i] = 1
                else:
                    switch[i] = 0

    # 여학생일 경우
    if s == 2:
        # 비교 가능한 범위 : 자기위치에서 양 끝 중에 더 짧은 길이
        c, d = number - 1, N - number
        if c < d:
            r = c
        else: 
            r = d
        max_r = 0  # 바꿀수있는 최대 길이의 스위치 범위
        # 스위치 범위 구하기
        for j in range(0, r+1):
            a = switch[number-j-1:number]
            b = switch[number-1:number+j][::-1]
            if a == b:
                max_r = j
            else:
                break
        # 구한 범위를 이용해서 스위치 켜고 끄기
        for k in range(number-max_r-1, number+max_r):
            if switch[k] == 0:
                switch[k] = 1
            else:
                switch[k] = 0

# 엠엠에서 주워들은 수인이의 힌트
for l in range(N):
    print(switch[l], end = ' ')
    if (l + 1) % 20 == 0:
        print()
