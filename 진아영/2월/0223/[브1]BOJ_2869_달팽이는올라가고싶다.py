# 메모리 31120 KB, 시간 40 ms

#-----------------틀린코드--------------------------------
day, night, V = list(map(int, input().split()))

V -= day                # 처음 한 생각은 마지막날에 안미끄러지니까 마지막날에 올라갈 길이를 미리 빼주고
result = 1              # result에 1을 할당한 채로 시작하는 거였음 -> 답 다 나오는데 틀림! 왜 틀렸는지 아직 모르겠음
one_day = day - night   # 하루동안 이동하는 높이

if V % one_day == 0:            # 하루동안 이동할 높이를 나눠주고
    result += (V // one_day)    # 자투리가 없으면 그대로
else: 
    result = V + (V // one_day + 1)    # 자투리가 있으면 +1 ( 5 1 6 같은 테케에서 적용 )
print(result)

#-----------------맞은 코드--------------------------------

day, night, V = list(map(int, input().split()))
V -= night              # 그래서 이제 올라가야할 높이에서 마지막날 안미끄러지니까 올라가야할 높이에서 그만큼 빼주고 시작함
one_day = day - night   # 하루동안 이동하는 높이

if V % one_day != 0:              # 하루 이동할 높이를 나눠주고
    result = V // one_day + 1     # 자투리가 있으면 추가로 +1
else:
    result = V // one_day         # 자투리가 없으면 그대로

print(result)
