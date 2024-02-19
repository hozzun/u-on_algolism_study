# swea 1976번 시각덧셈 메모리 45028kb 실행시간 101ms
T = int(input())
for tc in range(1, T+1):
    time = list(map(int, input().split()))
    hour1 = 0
    min1 = 0
    hour = [time[0], time[2]] # hour 리스트 만들어줌
    min = [time[1], time[3]] # min리스트 만들어줌 
    for i in hour:
        hour1 += i # hour1에 더해줌
        if hour1 > 12: # 처음에 그냥 했는데 13시 이렇게 나와서 바꿔줌 .. 
            hour1 -= 12 # 더한게 12보다 크면 12를 빼서 출력해줘~
    for j in min:
        min1 += j # min1에 더해줌
        if min1 >= 60: # min이 60보다 크거나 같으면 
            hour1 += 1 # 시간에 1 더해주고
            min1 -= 60 # 분은 60 빼줘~ 

    print(f"#{tc} {hour1} {min1}") 
