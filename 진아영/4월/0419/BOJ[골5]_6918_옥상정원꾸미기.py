# 첨엔 for문으로 완전탐색했는데 시간초과나서 3일동안 고민함..
# 스택문제길래 스택만 생각해봐서 풀었삼
# 파이파이 116652 KB, 172 ms
# 파이썬   34556 KB, 3168 ms

N = int(input())
city = [int(input()) for _ in range(N)]

buildings = []  # 현재 건물을 볼 수 있는 건물들 후보가 담긴 스택
                # -> for문 한번만 돌려면 (N이 10억인가? 뭐 그래서) 현재 건물을 볼 수 있는 건물을 세줘야할거같았음
building = 0    # answer

for i in range(N):
    while buildings:  # 후보군이 있으면
        if buildings[-1] <= city[i]:   # 끝부터 비교해주면서 현재 건물을 볼 수 없는 조건인지 확인
            buildings.pop()            # 볼 수 없으면 pop
        else:                          # 볼 수 있으면
            break                      # 넘김 (어차피 뒤에 건물들은 다 볼 수 있으므로 검사 x)
          
    building += len(buildings)  # 현재 건물 볼 수 있는 건물들만 남은 후보 answer에 추가
    buildings.append(city[i])   # 현재 빌딩 후보에 넣기

print(building)
