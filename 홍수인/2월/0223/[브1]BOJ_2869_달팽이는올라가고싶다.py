# 테케 다 나오는데.... 반례를 도저히 못 찾겠음요...... 같이 찾아주삼.....ㅜㅡㅜㅡㅜㅡㅜㅡㅜㅡㅡㅜㅜㅜㅜㅜㅜㅠㅠㅠ

a, b, v = list(map(int, input().split()))
cycle = a-b

if (v-a) // cycle == 0 or (v-a) % cycle > 0:
    result = (v-a) // cycle + 2
elif (v-a) // cycle > 0:
    result = (v-a) // cycle + 1
elif a >= v:
    result = 1
elif v % cycle == 0 and cycle * (v // cycle -1) + a >= v:
    result = (v-a)//cycle

print(result)
