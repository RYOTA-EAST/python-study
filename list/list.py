a = "10 20 30"
b = "20 30 40"

# 文字列をスペースで区切る
print(a.split())
print(type(a.split()))

aa = a.split()
bb = b.split()

print(aa, bb)

# 区切った文字列を計算して文字列として格納する
combined1 = [str(int(x) - int(y)) for (x, y) in zip(aa, bb)]
print(combined1)