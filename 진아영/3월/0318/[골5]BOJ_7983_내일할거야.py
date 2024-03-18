# 파이파이 218060 KB, 3196 ms, 334 B

N = int(input())
homework = []  # (마감기한, 과제 걸리는 시간)

for _ in range(N):
    d, t = map(int, input().split())
    homework.append((t, d))   # sort 키값대로 정렬하는 법 몰라서 순서 바꿔서 append 해줌

homework.sort(reverse=True)   # 마감기한 순으로 정렬

rest = 9999999999999999    # 최소 쉬는날

for i in homework:
    if i[0] >= rest:           # 최소 쉬는날보다 마감 기한이 더 크면
        rest -= i[1]           # 그 최소쉬는날에 공부할 날짜 빼줌
    else:                      # 그렇지 않으면
        rest = i[0] - i[1]     # 기존 값 버리고 새로 저장

print(rest)
