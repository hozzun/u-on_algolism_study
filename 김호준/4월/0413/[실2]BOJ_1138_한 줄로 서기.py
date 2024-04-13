# Python 메모리: 31120KB, 시간: 48ms, 코드 길이: 291B

N = int(input())
arr = list(map(int, input().split()))
ans = [False] * N

for i in range(N):
    check = 0
    for j in range(N):
        if arr[i] == check and not ans[j]:
            ans[j] = i + 1
            break

        elif arr[i] != check and not ans[j]:
            check += 1

print(*ans)

# 이 문제 한 1시간 가까이 고민한듯 어렵네 ...
# check 값으로 카운트해서 인덱스 이용해서 풀었삼 1~N 순서대로 라고해서 이거 말곤 없는거 같음 ..
