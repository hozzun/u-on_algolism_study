garo, sero = list(map(int, input().split()))
dot = int(input())

garo_lst = []
sero_lst = []
max_garo = 0
max_sero = 0

for i in range(dot):
    # dir : 가로(0) or 세로(1)
    # position : 자르는 위치
    dir, position = list(map(int, input().split()))

    if dir == 0:  # 한줄씩 입력받은 position을 가로, 세로 구분하여 각 리스트에 추가.
        garo_lst.append(position)
    else:
        sero_lst.append(position)

# 마지막 자르는 위치는 종이 크기에서 빼야 길이 구할 수 있으므로 첫 줄에서 입력받은 종이의 전체 가로, 세로를 리스트의 마지막에 추가.
garo_lst.append(sero)  
sero_lst.append(garo)
garo_lst.sort()
sero_lst.sort()

for i in range(len(garo_lst)):   # 가로 리스트 요소를 순회하며 최대 길이(인접 인덱스 간의 차) 구함
    if i==0:
        val = garo_lst[0] - 0
    else:
        val = garo_lst[i] - garo_lst[i-1]
    
    if val > max_garo:
        max_garo = val
        
for j in range(len(sero_lst)):   # 세로 리스트에서 최대 길이 구하기
    if j == 0:
        val = sero_lst[0] - 0
    else:
        val = sero_lst[j] - sero_lst[j-1]
    if val > max_sero:
        max_sero = val
        
print(max_sero * max_garo)  # 가로, 세로 각 최대 길이의 변이 이루는 직사각형의 넓이 == 가장 큰 종이의 넓이
