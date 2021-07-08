import contextlib

# def tag(name):
#     def _tag(f):
#         def _wrapper(context):
#             print('<{}>'.format(name))
#             r = f(context)
#             print('</{}>'.format(name))
#             return r
#         return _wrapper
#     return _tag
#
# @tag('h2')
# def f(context):
#     print(context)
#
#
# # f = tag(f)
#
# f('test')

# 上記を簡易化
@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield
    print('</{}>'.format(name))

# @tag('h2')
# def f(context):
#     print(context)
#
# f('test')
# ネストする
def f():
    with tag('h2'):
        print('test')
        with tag('a'):
            print('test')

f()
