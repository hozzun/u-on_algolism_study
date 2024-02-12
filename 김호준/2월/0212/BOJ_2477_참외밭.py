K = int(input())

all = []
east_west = []
south_north = []
for _ in range(6):
    way, side = map(int, input().split())
    all.append(side)
    if way == 1 or way == 2:
        east_west.append(side)
    elif way == 3 or way == 4:
        south_north.append(side)

max_h = max(east_west)
max_w = max(south_north)
h_idx = all.index(max_h)
w_idx = all.index(max_w)

result_h = abs((all[(h_idx-1)%6]) - (all[(h_idx+1)%6]))
result_w = abs((all[(w_idx-1)%6]) - (all[(w_idx+1)%6]))

result = (max_h * max_w) - (result_h * result_w)
print(result * K)
