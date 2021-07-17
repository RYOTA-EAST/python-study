import collections

# a = {'a': 'a','c': 'c','num': 0}
# b = {'b': 'b','c': 'cc'}
# c = {'b': 'bbb','c': 'ccc'}

# class DeepChainMap(collections.ChainMap):
#     def __setitem__(self, key, value):
#         for mapping in self.maps:
#             if key in mapping:
#                 # そのkeyが存在して、値が大きい時更新
#                 if type(mapping[key]) is int and mapping[key] < value:
#                     mapping[key] = value
#                 return
#         # そのkeyがない場合作成
#         self.maps[0][key] = value
        
# m = DeepChainMap(a, b, c)
# m['new_num'] = -10
# m['new_num'] = -1
# m['new_num'] = -100
# print('0より小さいと変更されない', 'num:', m['num'])
# print('新しい値は作成される', 'new_num:', m['new_num'])

# print(a)
# a.update(b)
# print(a)
# a.update(c)
# print(a)

# m = collections.ChainMap(a, b, c)
# print(m)
# print(m.maps)
# m.maps.reverse()
# print('reverse::', m.maps)
# del m.maps[0]
# m.maps.insert(0, {'c': 'cccccc'})
# print(m.maps)
# print(m['c'])

### collections.defaultdict

# d = {}
# d = collections.defaultdict(int)
# l = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'c']

# for word in l:
#     if word not in d:
#         d[word] = 0
#     d[word] += 1

# for word in l:
#     d.setdefault(word, 0)
#     d[word] += 1

# for word in l:
#     d[word] += 1

# print(d)

# d = collections.defaultdict(set)
# s = [('red', 1), ('blue', 2), ('red', 4), ('red', 1), ('blue', 2)]
# for k, v in s:
#     d[k].add(v)
# print(d)

### collection.counter
# データをカウント
# l = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'c']

# c = collections.Counter()
# for word in l:
#     c[word] += 1
# print(c)
# print(c.most_common(2))
# print(sum(c.values()))
# # 正規表現でワードを抽出して使われてる回数の多い順番に表示
# import re
# with open('Collection.py', 'r') as f:
#     words = re.findall(r'\w+', f.read().lower())
#     print(collections.Counter(words).most_common(20))

### collections.deque
# import queue
# collections.deque

# q = queue.Queue()
# lq = queue.LifoQueue()
# l = []
# d = collections.deque()

# for i in range(3):
#     q.put(i)
#     lq.put(i)
#     l.append(i)
#     d.append(i)
    
# for _ in range(3):
#     print('FIF0 queue = {}'.format(q.get()))
#     print('LIF0 queue = {}'.format(lq.get()))
#     print('list       = {}'.format(l.pop(0)))
#     print('deque      = {}'.format(d.popleft()))
    # print()

# print(d)
# print(d[1])
# print(d[-1])

# print(d)
# d.rotate()
# print(d)
# d.rotate()
# print(d)
# d.rotate()

# d.extend('y')
# d.extendleft('x')
# print(d)

### collections.namedtuple
import csv

with open('name.csv', 'w') as csvfile:
    fieldnames = ['first', 'last', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first': 'mike', 'last': 'jackson', 'address': 'A'})
    writer.writerow({'first': 'jum', 'last': 'sakai', 'address': 'B'})
    writer.writerow({'first': 'nancy', 'last': 'mask', 'address': 'C'})

with open('name.csv', 'r') as f:
    csv_reader = csv.reader(f)
    print(csv_reader)
    Names = collections.namedtuple('Names', next(csv_reader))
    for row in csv_reader:
        names = Names._make(row)
        print(names.first, names.last, names.address)

# Point = collections.namedtuple('Point', 'x, y')
# p = Point(10, y=20)
# print(p.x)
# # p.x = 100

# p1 = Point._make([100, 200])
# print(p1)
# print(p1._asdict())

# p1._replace(x=500)
# print(p1)
# p2 = p1._replace(x=500)
# print(p2)

# class SumPoint(collections.namedtuple('Point', ['x', 'y'])):
#     @property
#     def total(self):
#         return self.x + self.y
# p3 = SumPoint(2, 3)
# print(p3.x, p3.y, p3.total)