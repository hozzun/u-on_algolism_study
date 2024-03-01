N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = -10000000

for i in range(N-M+1):
    # 이중for문 썼는데 시간초과나서 슬라이싱으로 바꿔봄 그래도 시간초과!
    arr_sum = sum(arr[i:i+M])

    if arr_sum > max_sum:
        max_sum = arr_sum

print(max_sum)
