# yieldが付くとgeneratorになる
# next()で次に移る
# 間に処理入れても覚えている
def counter(num = 4):
    for i in range(num):
        word = 'run' + str(i + 1)
        yield word


def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(c))
print('* * * * * * * * * * * *')
print(next(g))
print(next(c))
print(next(c))
print('* * * * * * * * * * * *')
print(next(g))

