# 드디어 성공 ..... 달팽이 개미워
# 메모리 108080 / 시간 108ms

a, b, v = list(map(int, input().split()))
cycle = a-b
# 212
if (v-a) != 0 and (v-a) // cycle == 0 or (v-a) % cycle > 0:
    result = (v-a) // cycle + 2
elif (v-a) // cycle > 0:
    result = (v-a) // cycle + 1
elif a >= v:
    result = 1
elif v % cycle == 0 and cycle * (v // cycle -1) + a >= v:
    result = (v-a)//cycle

print(result)
