# 호준오빠가 고쳐준 버전
# 파이파이 	110680 KB, 4220 ms


N = int(input()) # 크레인 수
weight_limit = list(map(int, input().split()))   # 무게제한
M = int(input()) # 박스 수
box_weight = list(map(int, input().split()))   # 박스 무게
weight_limit.sort(reverse=True)
box_weight.sort(reverse=True)
time = 0


if max(box_weight) > max(weight_limit):
    print(-1)

else:

    while box_weight:
        box_okay = 0
        for i in weight_limit:
            for j in range(len(box_weight)):
                if i >= box_weight[j]:
                    box_weight.remove(box_weight[j])
                    box_okay += 1
                    break
            if box_okay == N:
                break
        time += 1

    print(time)

#---------------------------실패 버전---------------------------

N = int(input()) # 크레인 수
weight_limit = list(map(int, input().split()))   # 무게제한
M = int(input()) # 박스 수
box_weight = list(map(int, input().split()))   # 박스 무게
weight_limit.sort(reverse=True)
box_weight.sort()
time = 0


if max(box_weight) > max(weight_limit):
    print(-1)

else:
    while box_weight:
        box_okay = 0
        for i in weight_limit:
            if box_weight:
                if i < box_weight[-1]:           # 크레인 무게보다 더 나가는 박스는
                    continue
                else:
                    box_weight.pop()
                    box_okay += 1
            if box_okay == N:
                break
        time += 1

    print(time)
