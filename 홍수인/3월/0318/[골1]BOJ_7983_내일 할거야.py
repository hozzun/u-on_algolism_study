n = int(input())
check = []
cnt = 0
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
arr.sort(key=lambda arr:arr[1], reverse=True)   # 마감일 기준 내림차순

for i in range(n-1):
    start = arr[i][0]
    end = arr[i][1]

    day = arr[i][1] - arr[i][0] + 1   # 시작일 = 0번행의 마감기한을 지키는 가장 늦은 시작일 ?
    if day <= arr[i+1][1]:
        cnt += arr[i+1][1] - day + 1
    else:
        continue
print(arr[n-1][1] - arr[n-1][0] - cnt)
