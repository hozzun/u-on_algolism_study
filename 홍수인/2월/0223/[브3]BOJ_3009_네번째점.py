# 메모리 108080 / 시간 108ms
x_lst = []
y_lst = []

for i in range(3):
    x, y = list(map(int, input().split()))
    x_lst.append(x)
    y_lst.append(y)

for i in x_lst:   # 입력받은 x좌표 리스트 순회
    if x_lst.count(i) == 1: # 개수가 1인 값 == 구하는 x 좌표
        result_x = i

for j in y_lst:   # 입력받은 y좌표 리스트 순회
    if y_lst.count(j) == 1:  # 개수가 1인 값 == 구하는 y 좌표
        result_y = j

print(result_x, result_y)
