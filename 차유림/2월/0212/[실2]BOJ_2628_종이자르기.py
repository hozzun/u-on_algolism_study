row , col = map(int, input().split())
k = int(input())
garo_list = []
saero_list = []
max_val = 0 # 최대 넓이 구해줄 변수 

for i in range(k):
    gs, line = map(int, input().split()) 
    if gs == 0: 
        saero_list.append(line) # 가로로 자른 부분이 세로가 되므로 세로 리스트에 넣어줌 
    else:
        garo_list.append(line) # 세로로 자른 부분이 가로가 되므로 가로 리스트에 넣어줌 
        
garo_list.append(0)
garo_list.append(row) # 가로 리스트에 0 과 row 값을 넣어줌 [0, 4, 10] 이 되게 
saero_list.append(0)
saero_list.append(col) # 세로 리스트에 0과 col 값을 넣어줌 [0, 2, 3, 8] 이 되게

garo_list.sort() # 정렬해줌 
saero_list.sort()

real_garo = []
real_saero = []
for i in range(1, len(garo_list)): # 진짜 가로 리스트는 4-0, 10-4값을 넣어줘야 함  
    garo = garo_list[i] - garo_list[i-1]
    real_garo.append(garo)

for i in range(1, len(saero_list)): # 진짜 세로 리스트는 2-0, 3-2, 8-3 값을 넣어줘야 함
    saero = saero_list[i] - saero_list[i-1]
    real_saero.append(saero)

for garo in real_garo: 
    for saero in real_saero:
        area = garo * saero # 가로 * 세로 값 곱해줌
        if max_val < area: # 최댓값 < 넓이 이면 
            max_val = area # 최댓값 = 넓이 값으로 저장해준다 

print(max_val)
        
