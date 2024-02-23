# 31120kb 40ms
# idea : 올라가고 내려가는 걸 하루라고 쳤을 때, 몫을 구하는 식으로 하자!
a, b, v = map(int, input().split())

v = v - a # 정상에 올라가면 안내려오므로 미리 빼줌
if v > 0: # 목표거리 보다 하루 올라가는 거리가 작은 경우
    if v >= (a-b):
        if v % (a-b) == 0:
            answer = v // (a-b) + 1
        else:
            answer = v // (a-b) + 2
    else:
        answer = 2
else: # 목표거리와 하루 올라가는 거리가 같은 경우
    answer = 1
print(answer)
