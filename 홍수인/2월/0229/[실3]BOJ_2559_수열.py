# 메모리 120956 / 시간 : 132ms

n, k = map(int, input().split())
arr = list(map(int, input().split()))
sum_val = sum(arr[:k])
pre_idx = 0
max_val = sum_val

for i in range(n-k):
    sum_val = sum_val - arr[pre_idx] + arr[i+k]  
    pre_idx += 1    # 더하는 구간의 첫번째 인덱스 저장.
    if sum_val >= max_val:   # 최대값 구하기
        max_val = sum_val

print(max_val)
