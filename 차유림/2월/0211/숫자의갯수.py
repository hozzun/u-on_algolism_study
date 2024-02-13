A = int(input()) 
B = int(input())
C = int(input())
num = A * B * C 
num1 = list(map(int,str(num))) # 하나하나 따로 해주기 위해서 map사용 
counts = [0] * 10 #counts 리스트 만들어서 해당 숫자 있으면 1 추가 
for i in num1:
  counts[i] += 1
for j in counts: # counts 리스트 나열 
  print(j)
