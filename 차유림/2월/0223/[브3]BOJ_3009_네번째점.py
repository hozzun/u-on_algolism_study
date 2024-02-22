# 백준 3009번 네 번째 점 메모리 31120 KB 시간 44ms

x = [] # x의 점 리스트 
y = [] # y의 점 리스트 

for i in range(3):
    arr = list(map(int, input().split()))
    x.append(arr[0]) 
    y.append(arr[1])
    
real_x = 0
real_y = 0
for i in x: # x가 1번 있는 것이 구해야 할 x좌표이다 
    if x.count(i) == 1:
        real_x = i

for i in y: # y가 1번 있는 것이 구해야 할 y좌표 
    if y.count(i) == 1:
        real_y = i

print(real_x, real_y)
