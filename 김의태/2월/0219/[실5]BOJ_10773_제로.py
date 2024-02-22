# 메모리 : 31900KB 시간 : 4004ms...?what the..
# idea : 전형적인 스택문제.
k = int(input())
k_list = []
for i in range(k): #스택...0이면 빼고 아니면 넣고..
    num = int(input())
    if num != 0:
        k_list.append(num)
    else:
        k_list.pop()
print(sum(k_list))
