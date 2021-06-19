# 変数宣言
num1 = 1
num2 = '1'
name = 'mike'
is_ok = True

new_num = int(num2)

# 型を調べる
print(new_num)
print(num1, type(num1))
print(name, type(name))
print(is_ok, type(is_ok))

print('Hi','Mike',sep=',',end='.\n')
print('Hi','Mike',sep=',',end='.\n')

print(17//3)
print(17%3)
print(5**5)

y = 10
x = 5
z = x + y
print(z)

pie =3.1415151515
print(pie)
print(round(pie,3))

import math

result = math.sqrt(25)
print(result)

# print(help(math))

print("""\
line1
line2
line3\
""")

word = "python"
print(word[0:2])
print(word[2:])

word = "j" + word[1:]
print(word)
print(len(word))

a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')
