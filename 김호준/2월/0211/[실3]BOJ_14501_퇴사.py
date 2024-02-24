def recur(idx, total):
    global answer

    if idx > N - 1:
        if idx > N:
            return
        answer = max(answer, total)
        return

    # 상담 했을 때
    recur(idx + arr[idx][0], total + arr[idx][1])
    # 상담 안했을 때
    recur(idx + 1, total)

N  = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
recur(0, 0)
print(answer)
