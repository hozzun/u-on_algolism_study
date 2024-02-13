A = int(input())
B = int(input())
C = int(input())
num = A * B * C 
num1 = list(map(int,str(num)))
counts = [0] * 10
for i in num1:
  counts[i] += 1
for j in counts:
  print(j)
