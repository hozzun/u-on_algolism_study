# .... 어떻게 정답을 내야 할지 도저히 생각이 안남 ㅎㅎ 포기~~

from collections import deque

def left(idx, dir):
    if idx < 0:
        return
    elif arr[idx][2] != arr[idx+1][6]:
        left(idx - 1, dir)
        arr[idx].rotate(dir)


def right(idx, dir):
    if idx > 3:
        return
    elif arr[idx][6] != arr[idx-1][2]:
        right(idx + 1, dir)
        arr[idx].rotate(dir)


arr = [deque(map(int, input().rstrip())) for _ in range(4)]

K = int(input())
for _ in range(K):
    num, direction = map(int, input().split())
    left(num - 1, direction)
    right(num + 1, direction)
    arr[num].rotate(direction)


