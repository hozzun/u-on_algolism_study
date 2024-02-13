N = int(input())
arr = []
length = []
long_r = 0
long_c = 0

for _ in range(6):
    a, m = list(map(int, input().split()))
    arr.append(a)
    length.append(m)

for i in range(6):
    if arr[i] == 3 and arr[i - 1] == 1:
        small_square = length[i] * length[i - 1]
    elif arr[i] == 1 and arr[i - 1] == 4:
        small_square = length[i] * length[i - 1]
    elif arr[i] == 4 and arr[i - 1] == 2:
        small_square = length[i] * length[i - 1]
    elif arr[i] == 2 and arr[i - 1] == 3:
        small_square = length[i] * length[i - 1]

for j in range(6):
    if arr[j] == 1 or arr[j] == 2:
        if long_r < length[j]:
            long_r = length[j]
    elif arr[j] == 3 or arr[j] == 4:
        if long_c < length[j]:
            long_c = length[j]

num = N * (long_c*long_r - small_square)

print(num)
