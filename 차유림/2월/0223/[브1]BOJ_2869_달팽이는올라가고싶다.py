# 2869번 달팽이는 올라가고 싶다 시간 초과남 멍미!!!!!!! 심지어 3번째 예제는 넣으면 결과 나오지도 않아 오래걸림 ;;;;;;; 
# while 안쓰고 어캐함????????????????????????????????????

A, B, V = map(int, input().split())
c = 0 # 현재위치
cnt = 0 # 일 수
while c < V: # c != V 하니까 무한루프 걸림 ㅜㅜ
    if A >= V: # A가 5보다 크면
        cnt = 1 # 일 수는 1 이고
        break # 멈춤
    elif A < V: # A가 V보다 작으면 
        c += A # 현재위치에 A 더해줌 
        if c < V: # 만약에 현재위치가 V보다 작으면 
            c -= B # 현재위치에 B 뺴주고
            cnt += 1 # 일수를 더한다 
        elif c >= V: # 만약에 현재 위치가 V보다 크다면 
            cnt += 1 # 일 수 더하고 
            break # 멈춤 

print(cnt)

# -----------------------------------------------------------------

# 메모리 31120kb 시간 40ms
A, B, V = map(int, input().split())
day = V - B 
cycle = A - B
result = 0
if day % cycle != 0:
    result = day // cycle + 1
else:
    result = day // cycle 

print(result)
