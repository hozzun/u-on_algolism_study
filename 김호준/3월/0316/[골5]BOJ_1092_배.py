# PyPy3 메모리: 110592KB, 시간: 4412ms, 코드 길이: 442B

N = int(input())
limit = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

limit.sort(reverse=True)
box.sort(reverse=True)

if box[0] > limit[0]:
    print(-1)

else:
    answer = 0
    while box:
        for i in range(N):
            for j in range(len(box)):
                if limit[i] >= box[j]:
                    box.remove(box[j])
                    break
        answer += 1

    print(answer)
