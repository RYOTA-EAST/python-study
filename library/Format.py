print('{2}, {0}, {1}'.format('a', 'b', 'c'))

print('{name}, {family}'.format(name='ryota', family='higashi'))

t = (1, 2, 3)
print('{0[0]}'.format(t))
# *t はタプルを展開　(1, 2, 3)
print('{0}, {2}'.format(*t))

d = {'name': 'ryota', 'family': 'higashi'}
print('{name}, {family}'.format(**d))

# 30文字の間でどこに何を、残りは何で埋めるか
print('{:#<30}'.format(' left '))
print('{:#>30}'.format(' right '))
print('{name:{fill}{align}{width}}'.format(name=' center ', fill='#', align='^', width=30))

print('{:,}'.format(123456789))
print('{:+f} {:+f}'.format(3.14, -3.14))

print('{:.2%}'.format(19 / 22))

print(int(100), hex(100), oct(100), bin(100))
print('{0:d} {0:x} {0:o} {0:b}'.format(100))

for i in range(20):
    for base in 'bdX':
        print('{:5{base}}'.format(i, base=base), end=' ')
    print()