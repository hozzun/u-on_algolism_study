# 나 이거 왜 틀리는지 도저히 모르겠음 43% 에서 틀림
# 찾아냈음
# 리턴에서 max(max_v, total) 로 하면 틀림 max(total, max_v)로 하면 정답이고
# 뭔 차이임;; 어차피 둘 중에 큰거 구하는건데 화나네

# Python 메모리: 31120KB, 시간: 60ms, 코드길이: 723B

def recur(idx, total, plus, minus, mul, div):
    global max_v, min_v
    if idx == N: # 인덱스 끝에 찍으면 리턴
        max_v = max(total, max_v)
        min_v = min(total, min_v)
        return

    if plus > 0: # 0 보다 클 때만
        recur(idx + 1, total + arr1[idx], plus - 1, minus, mul, div)
    if minus > 0:
        recur(idx + 1, total - arr1[idx], plus, minus - 1, mul, div)
    if mul > 0:
        recur(idx + 1, total * arr1[idx], plus, minus, mul - 1, div)
    if div > 0: # 첨에 // 로 했는데 예시문제 음수 나눗셈 원하는 몫 안나와서 바꿈
        recur(idx + 1, int(total / arr1[idx]), plus, minus, mul, div - 1)


N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

max_v = -1e9 # 초기 값
min_v = 1e9

recur(1, arr1[0], arr2[0], arr2[1], arr2[2], arr2[3])

print(max_v)
print(min_v)
