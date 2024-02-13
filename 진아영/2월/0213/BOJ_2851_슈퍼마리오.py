num_lst = []
num_sum = 0

for i in range(10):
    num_lst.append(int(input()))   # 10개의 버섯 리스트로 할당

for num in num_lst:
    num_sum += num      # 버섯 먹기 시작
    if num_sum >= 100:  # 만약 버섯먹다가 100점이 넘으면
        break           # 중단

# 가장 최근에 먹은 버섯과 바로 직전에 먹은 버섯중 뭐가 더 100과 차이가 안나는지 비교
if abs(num_sum - 100) <= abs(num_sum - num - 100):    # 똑같이 차이가 난다면 더 큰 점수가 선택되도록 조건 설정
    print(num_sum)                                    # 더 큰 점수 출력

else:
    print(num_sum - num)
