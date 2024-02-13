row , col = map(int, input().split())
k = int(input())
garo_list = []
saero_list = []
max_val = 0 # 최대 넓이 구해줄 변수 

for i in range(k):
    gs, line = map(int, input().split())
    if gs == 0: 
        saero_list.append(line)
    else:
        garo_list.append(line)
        
garo_list.append(0)
garo_list.append(row)
saero_list.append(0)
saero_list.append(col)

garo_list.sort()
saero_list.sort()

real_garo = []
real_saero = []
for i in range(1, len(garo_list)):
    garo = garo_list[i] - garo_list[i-1]
    real_garo.append(garo)

for i in range(1, len(saero_list)):
    saero = saero_list[i] - saero_list[i-1]
    real_saero.append(saero)

for garo in real_garo:
    for saero in real_saero:
        area = garo * saero
        if max_val < area:
            max_val = area

print(max_val)       
