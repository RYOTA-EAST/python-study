import math

nums = [11, 23, 22, 11]

# 配列の真ん中の値を取得
nums_len = len(nums)
center = math.ceil((nums_len) / 2) - 1
print("centerは", center)

# 中央値設置→配列数が奇数なら真ん中の値、偶数なら真ん中2つの平均
if nums_len % 2 == 0:
  center_num = math.ceil((nums[center] + nums[center + 1]) / 2)
  print("配列は偶数で、中央値は", center_num)
else:
  center_num = nums[center]
  print("配列は奇数、中央値は", center_num)

# 配列の最初の偶数を探す
for num in nums:
  if num % 2 == 0:
    print(num, "は最初の偶数です")
    judge_num = num
    break

# 中央値と最初の偶数を比較
if judge_num >= center_num:
  print("true")
else:
  print("false")


# roundの四捨五入の丸め処理は偶数
print(round(3.5))  # OUT: 4
print(round(2.5))  # OUT: 2
print(round(1.5))  # OUT: 2

import math
print(math.ceil(2.5)) # OUT: 3