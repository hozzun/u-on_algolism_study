# 실버 1 카드 합체 놀이
# 메모리 31120kb 시간 180ms 코길 229

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(m):
    new_num = arr[0] + arr[1]
    arr[0] = new_num
    arr[1] = new_num
    arr.sort()

print(sum(arr))
