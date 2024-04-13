# 한줄로서기 
# 흠.. 예전에 2605번이랑 푼거랑 비슷해서 그렇게 풀어봤는데 안되네 ㅠ.......

N = int(input())
height = list(map(int, input().split()))
lst = []
for i in range(N):
    lst.insert(height[i], i + 1)

print(' '.join(map(str, lst)))
