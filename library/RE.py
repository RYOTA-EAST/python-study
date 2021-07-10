import re
# m = re.match('a.c', 'abc')
# print(m.group())

# m = re.search('a.c', 'test abc test abc')
# print(m)
# print(m.span())
# print(m.group())

# m = re.finditer('a.c', 'test abc test abc')
# print([w.group() for w in m])
# print([w.span() for w in m])

# m = re.match('ab?', 'abb')
# m = re.match('ab*', 'abb')
# m = re.match('ab+', 'abb')
# m = re.match('a{2,4}', 'aaa')
# m = re.match('[a-zA-Z0-9_]', '_') # 半角英数字
# m = re.match('[^a-zA-Z0-9_]', '@')
# m = re.match('\w', '_')
# m = re.match('\W', '@')
# m = re.match('\d', '1') # 数字であるか
# m = re.match('\D', 'a') # 数字でない（大文字は反転）
# m = re.match('a|b', 'a') # a or b
# m = re.match('(abc)+', 'abcabc') # abcが1回以上
# m = re.match('\s', ' ') # スペース
# m = re.match('\*', '*') # *は意味を持つのでバックスラッシュをつける
# m = re.search('abc$', 'abctest abctest') # ^は先頭　$は最後
# print(m)

### group compile VERBOSE

# RE_STACK_ID = re.compile(r"""
#         arn:aws:cloudformation:
#         (?P<region>[\w-]+):       # region
#         (?P<account>[\d]+)        # account
#         :stack/
#         (?P<stack_name>[\w-]+)/   # stack_name
#         [\w-]+""", re.VERBOSE)

# s1 = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
# 'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')
# s2 = ('arn:aws:cloudformation:us-east-1:123456789012:stack/'
# 'mystack-mynestedstack-sggfrhxhaaaa/f449b250-b969-11e0-a185-5081d0136786')

# for s in [s1, s2]:
#     m = RE_STACK_ID.match(s)
#     if m:
#         print('go next')
#         print(m.group('region'))
#         print(m.group('account'))
#         print(m.group('stack_name'))
#     else:
#         raise Exception('Error!')

### split compile
# s = 'My name is ... Mike'
# print(s.split())

# p = re.compile(r'\W+')
# print(p.split(s))

# p = re.compile('(blue|white|red)')
# print(p.subn('color', 'blue socks and red shoes'))
# print(p.sub('color', 'blue socks and red shoes', count=1))

# def hexrepl(match):
#     value = int(match.group())
#     return hex(value)

# p = re.compile(r'\d')
# print(p.sub(hexrepl, '12345 55 11 test test2'))

### Greedy
# s = '<html><head><title>Title</title></head></html>'

# print(re.match('<.*>', s))
# print(re.match('<.*?>', s))