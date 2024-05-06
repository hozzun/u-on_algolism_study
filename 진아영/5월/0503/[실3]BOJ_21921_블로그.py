# 파이썬    58780 KB, 204 ms
# 파이파이 156496 KB, 180 ms
# 범위 보고 시간초과 날거같아서 호준오빠가 예전에 알려준 누적합으로 특정 범위 최댓값 구하기 생각나서 풀어봄

N, X = map(int, input().split())            # N일차, X일동안
todays = list(map(int, input().split()))    # N일동안 방문자 수
accum_todays = [0] * N                      # 새로운 누적합 배열
max_todays = 0
max_count = 0

for i in range(N):
    accum_todays[i] = accum_todays[i-1] + todays[i]  # 새로운 누적합

    # X일 누적합이 쌓였을 때부터
    if i >= X-1:
        if max_todays == accum_todays[i]-accum_todays[i-X]:
            max_count += 1
        elif max_todays < accum_todays[i]-accum_todays[i-X]:
            max_todays = accum_todays[i]-accum_todays[i-X]
            max_count = 1
    
if max_todays:
    print(max_todays)
    print(max_count)
else:
    print('SAD')


# -----근데 이건 왜 틀렸지? 맨 첨엔 누적합 배열 새로 안만들고 있던거 초기화해서 했는뎁..------------
# 64퍼센트 틀렸습니다

N, X = map(int, input().split())  # N일차, X일동안
todays = list(map(int, input().split()))  # N일동안 방문자 수
max_todays = 0
max_count = 0

if set(todays) == {0}:
    print('SAD')
    exit(0)

for i in range(1, N):
    todays[i] = todays[i-1] + todays[i]
    if i > X-1:
        if max_todays == todays[i]-todays[i-X]:
            max_count += 1
        elif max_todays < todays[i]-todays[i-X]:
            max_todays = todays[i]-todays[i-X]
            max_count = 1

print(max_todays)
print(max_count)
