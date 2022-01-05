# 配列を順番に出力
def printList(str_list):
  for str_list in str_lists:
    print(str_list)

# 配列値の合計を算出
def allSum(int_list):
  sum = 0
  for i in int_list:
    sum += i
  return sum

# 辞書型を判定
def intJudge(dict):
  for k, v in dict.items():
    if v == 20:
      print("値が20になるのは「", k, "」です")
    else:
      print("「", k, "」の値は20ではありません")

if __name__ == '__main__':
  str_lists = ["A", "happy", "new", "year"]
  printList(str_lists)

  dict = {'techacademy': 10, 'online': 20, 'programming': 30}
  intJudge(dict)

  import random
  # aaa = ["1", "2", "3"]
  # aaa = list(map(int, aaa))

  # 1000までの数値をランダムに配列に入れる
  aaa = [random.randint(0, 1000) for i in range(10) if i % 2 == 0]
  aaa.sort()
  print(aaa)

  all_sum = allSum(aaa)
  print(all_sum)
