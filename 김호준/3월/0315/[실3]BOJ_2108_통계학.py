# Python 메모리: 52504KB, 시간: 476ms, 코드 길이: 629B
# 왜 sys하면 시간초과 안나고 왜 sys하면 맞는지를 모르겠네..

import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    num = int(input())
    arr.append(num)

arr.sort()

# 산술 평균
answer1 = round(sum(arr) / N)
print(answer1)

# 중앙 값
answer2 = arr[N//2]
print(answer2)

# 최빈 값
cnt = dict()
for i in arr:
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1

max_cnt = max(cnt.values())
answer3 = []
for key, val in cnt.items():
    if val == max_cnt:
        answer3.append(key)

answer3.sort()

if len(answer3) == 1:
    print(answer3[0])
else:
    print(answer3[1])

# 범위
answer4 = abs(arr[0] - arr[-1])
print(answer4)
