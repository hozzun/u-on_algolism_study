# 파이파이  113144 KB, 200 ms, 979 B
# 파이썬    	 31252 KB, 68 ms



N = int(input())   # 수의 개수
num_list = list(map(int, input().split()))   # 숫자
unit_1 = list(map(int, input().split()))  # 연산자 수 ( +, -, *, / )
unit_2 = unit_1
max_num = -1000000000
min_num = 1000000000

def calculate(i, n):
    global min_num, max_num

    if i == N:
        if n < min_num:
            min_num = n
        if n > max_num:
            max_num = n
        return
      

    for j in range(4):
        if unit_1[j]:
            unit_1[j] -= 1         # 하나 사용한 표시

            # 연산자별 계산 내용
            if j == 0:
                calculate(i+1, n + num_list[i])
            elif j == 1:
                calculate(i + 1, n - num_list[i])
            elif j == 2:
                calculate(i + 1, n * num_list[i])
            elif j == 3:
                if n < 0:          # 음수 나누기 조건 설정
                    calculate(i + 1, (n * (-1) // num_list[i]) * (-1))
                else:
                    calculate(i + 1, n // num_list[i])
                  
            unit_1[j] += 1         # 사용 표시 초기화



calculate(1, num_list[0])    # 초기값 숫자 리스트의 첫번째 숫자부터 넣고 시작

print(max_num)
print(min_num)
