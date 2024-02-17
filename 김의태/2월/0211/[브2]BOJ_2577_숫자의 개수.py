abc = [int(input()) for _ in range(3)]

multiple = str(abc[0]*abc[1]*abc[2])

idx = 0
while idx < 10:
    cnt = 0
    for num in multiple:
        if idx == int(num):
            cnt += 1
    print(cnt)
    idx += 1
