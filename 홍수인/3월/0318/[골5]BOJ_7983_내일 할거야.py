# 메모리: 239808, 시간 : 3076ms, 코드 길이: 378B

n = int(input())
check = []
cnt = 0
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
arr.sort(key=lambda arr:arr[1], reverse=True)   # 마감일 기준 내림차순 정리

day = arr[0][1]      # 놀 수 있는 마지막 날
for i in range(n):    # 과제 목록에 하나씩 접근
    start = arr[i][0]
    end = arr[i][1]

    if day >= end:    # 겹치지 않는(?) 경우
        day = end - start     # 그 과제가 걸리는 기간 만큼? 앞당김.
    else:            # 겹치는 경우
        day = day - start     # 현재 day에서 기간을 빼줌. (말로 설명을 잘 못하겠네....)
print(day)
