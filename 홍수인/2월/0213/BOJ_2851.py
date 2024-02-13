arr = []

for i in range(10):
    a = int(input())
    arr.append(a)

sum_val = 0
diff = 101

for i in range(10):
    sum_val += arr[i]   # 순차적으로 누적 합
    if abs(100-sum_val) <= diff:  # 누적할 때마다 100과의 차이를 구해 100과 가장 가까운 누적 합의 값을 저장.
        diff_i = sum_val  # 100과 가장 가까운 수가 되었을 때, 그때의 sum_val을 출력
print(diff_i)
