# リストは配列
i = [1, 2, 3, 4, 55]
j = i
j[0] = 100
print('参照渡しは値を渡す')
print('j=', j)
print('j(id)=', id(j))
print('i=', i)
print('i(id)=', id(i))

x = [1, 2, 3, 4, 55]
y = x.copy()
y[0] = 100
print('copyは値渡し')
print('x=', x)
print('x(id)=', id(x))
print('y=', y)
print('y(id)=', id(y))

# タプルは変更できないリストのようなもの
t = 1,
print(type(t))

# 型をタプルであれば変更可能入れ替えを簡単にできる
a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

# 辞書型はキーとバリューで管理
d = {'apple': 100,
     'banana': 200,
     'orange': 500
     }
print(d, type(d))
print('りんごは', d['apple'], '円です')

# 集合型は配列を比較、重複の省略ができる
my_friends = {'a', 'b', 'c', 'c', 'd'}
print(my_friends)
you_friends = {'b', 'c', 'd', 'f'}
print(you_friends)
print('重複している友人は', my_friends & you_friends, 'です')