# 121552 KB, 132 ms

N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = sum(arr[0:M])
new_sum = sum(arr[0:M])

for i in range(1, N-M+1):
    # 이중for문 썼는데 시간초과나서 슬라이싱으로 바꿔봄 그래도 시간초과!
    # arr_sum = sum(arr[i:i+M])

    # 그래서 이렇게 바꿔줌
    # new_sum = 바로전의 구간합 - (바로전의 구간합 첫번째 원소) + (현재의 구간합 마지막 원소)
    new_sum = new_sum - arr[i-1] + arr[i+M-1]
    if new_sum > max_sum:
        max_sum = new_sum
    
print(max_sum)
