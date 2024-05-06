# X일 동안 가장 많이 들어온 방문자 수와 기간이 몇개 있는지 구하자

# 블로그를 시작하고 지난 일수 N과 X
N, X = map(int, input().split())
# 블로그 시작 1일차부터 N일차까지 하루 방문자 수
arr = list(map(int, input().split()))

visitors = []
for i in range(1, N-X+1):
    visitors.append(sum(arr[i:i+X]))

# 최대 방문자 수 0명이면 SAD 출력
if max(visitors) == 0:
    print('SAD')
else:
    # X일 동안 가장 많이 들어온 방문자 수
    print(max(visitors))
    # 만약 최대 방문자 수가 0명이 아닌 경우 기간이 몇개 있는지 출력
    print(visitors.count(max(visitors)))
