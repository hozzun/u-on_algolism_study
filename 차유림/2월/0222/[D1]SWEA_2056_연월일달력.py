# swea 2056 연월일 달력 메모리 58544 kb 시간 168ms
T = int(input())
for tc in range(1, T+1):
    date = input() 
    year = date[:4] # 슬라이싱으로 연 월 일 나눠줌 
    month = date[4:6]
    day = date[6:8]
    month_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # 월 리스트 만들어줌 
    
    a = int(month)  # 아영언니가 힌트줌 ㅎㅎ 떙베감 ㅜㅜ 
    b = int(day)

    if a not in month_lst: # 월 리스트에 월이 없으면 
        print(f"#{tc} {-1}") # -1 출력 

    else: # 월 리스트에 월이 있으면 
        if a == 2: # 2월일때 
            day_lst = [i for i in range(1, 29)] # 일 리스트는 1~ 28 까지 
            if b not in day_lst: # 일이 일 리스트에 없으면 
                print(f"#{tc} {-1}") # -1 출력 
            else:
                print(f"#{tc} {year}/{month}/{day}") # 리스트에 있으면 날짜 출력

        elif a in [4, 6, 9, 11]: # 이 달은 일이 30 일 까지 
            day_lst = [i for i in range(1, 31)]
            if b not in day_lst:
                print(f"#{tc} {-1}")
            else:
                print(f"#{tc} {year}/{month}/{day}")

        else:
            day_lst = [i for i in range(1, 32)] # 나머지 월은 31 일 까지 
            if b not in day_lst:
                print(f"#{tc} {-1}")
            else:
                print(f"#{tc} {year}/{month}/{day}")
