# Python 메모리: 40156KB, 시간: 100ms

N, K = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(N+1)] # 누적합 배열 만들기

for i in range(N):
    prefix[i+1] = prefix[i] + arr[i] # 누적합 추가
# -> [0, 3, 1, -3, -12, -12, -9, -2, 11, 19, 16]

answer = []
for j in range(K, N+1):
    answer.append(prefix[j] - prefix[j-K])
    # 누적 합의 (j-k번째 값 - j번째 값) = 원하는 값(sum(arr[i:i+K]))

print(max(answer)) # 최대 값 출력
