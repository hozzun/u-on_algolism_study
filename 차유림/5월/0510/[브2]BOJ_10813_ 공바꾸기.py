# 10813 번 공 바꾸기 
# 메모리 31120 시간 44 코드길이 225
# 흠 .. 하운오빠가 풀었길래 넣었는데 너무 쉽네 ㅎㅎ;; 연습문제라 생각하자~~ 
N, M = map(int, input().split())
arr = [0]
for i in range(1, N + 1):
    arr.append(i)

for i in range(M):
    i, j = map(int, input().split())
    arr[i] , arr[j] = arr[j], arr[i]

print(*arr[1:])
