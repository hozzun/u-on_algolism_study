# Python 메모리: 31120KB, 시간: 40ms

'''
5 5
5 7
7 5 일 때 왼쪽을 x 오른쪽을 y로 하면
답 : 7 7 이면
5 2개 7 2개로 되서 이걸로 품
'''
x_arr = [] # x 집합
y_arr = [] # y 집합
for _ in range(3):
    x, y = map(int, input().split())
    x_arr.append(x) # x 집합에 넣음
    y_arr.append(y) # y 집합에 넣음

for i in x_arr:
    if x_arr.count(i) != 2: # 2개 없으면
        x_arr.append(i) # 넣어

for i in y_arr:
    if y_arr.count(i) != 2: # 2개 없으면
        y_arr.append(i) # 넣어

x_ans = x_arr.pop() # 넣은거 출력
y_ans = y_arr.pop() # 넣은거 출력
print(x_ans, y_ans)
