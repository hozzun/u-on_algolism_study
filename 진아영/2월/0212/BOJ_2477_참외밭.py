N = int(input())
arr = []
length = []
long_r = 0
long_c = 0

for _ in range(6):
    a, m = list(map(int, input().split()))
    arr.append(a)
    length.append(m)

for i in range(6):     # 육각형을 돌면서 반시계 방향이 아닌 시계방향 움직임 찾기 -> 그부분이 빵꾸난 부분 -> 그부분의 넓이 구하기 (small_square)
    if arr[i] == 3 and arr[i - 1] == 1:
        small_square = length[i] * length[i - 1]
    elif arr[i] == 1 and arr[i - 1] == 4:
        small_square = length[i] * length[i - 1]
    elif arr[i] == 4 and arr[i - 1] == 2:
        small_square = length[i] * length[i - 1]
    elif arr[i] == 2 and arr[i - 1] == 3:
        small_square = length[i] * length[i - 1]

for j in range(6):     # 육각형 중에 가장 긴 가로와 세로 길이 찾기
    if arr[j] == 1 or arr[j] == 2:
        if long_r < length[j]:
            long_r = length[j]
    elif arr[j] == 3 or arr[j] == 4:
        if long_c < length[j]:
            long_c = length[j]

num = N * (long_c*long_r - small_square)   # 참외 * (큰 네모 - 작은 네모)

print(num)
