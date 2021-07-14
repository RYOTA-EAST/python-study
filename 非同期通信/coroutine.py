def s_hello():
    yield 'hello1'
    yield 'hello2'
    yield 'hello3'
    return 'done'

def g_hello():
    """
    docstringは__doc__属性に文字列として格納されている。print()で出力できる。
    「カウントダウンしてhelloて表示する」の様に関数の説明を記述
    """
    while True:
        # print('3')
        print('2')
        # print('1')
        # s_helloの次のyeildを読み出す
        r = yield from s_hello()
        print('A')
        print('B')
        print('C')
        yield r

g = g_hello()

# print(g_hello.__doc__)
# 次のyieldまで実行
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# print(g.send('jun'))