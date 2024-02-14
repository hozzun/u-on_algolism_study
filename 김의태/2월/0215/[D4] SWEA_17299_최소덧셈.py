T = int(input())
for i in range(1, T + 1):
  num_str = input()
  ans = 99999999999999999
  for j in range(1, len(num_str)):
    a = int(num_str[:j])
    b = int(num_str[j:]) # 덧셈기호 넣기
    if ans > a + b: #덧셈기호 다른 위치에 넣을 때마다 최소값 알아보기
      ans = a + b
  print(f'#{i} {ans}')
