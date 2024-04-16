# 실패
# 테케는 맞음....
# 모르겠당 ~...

n = int(input())
arr = list(map(int, input().split()))

line = [0]*n
for i in range(n):
    idx = arr[i]
    if line[idx] == 0:
        line[idx] = i+1
    else:
        cnt = 0
        for j in range(n):
            if line[j] == 0:
                cnt += 1
                if cnt == idx+1:
                    line[j] = i+1
                    break
print(*line)
