# задание № 1: словарь изменяемый тип
# задание № 2
d = {'a': 1, 'b': 2}
print(d['b'])
# задание № 3
d = {'a': 1, 'b': 2}
print(d.keys())
# задание № 4
d = {'a': 1, 'b': 2}
print(d['a'], d['b'])
# задание № 5
d = {'a': 1, 'b': 2}
d['t'] = 1000
print(d)
# задание № 14
a = [1, 2, 3, 4]
d = dict.fromkeys([a[0], a[1], a[2], a[3]])
print(d, type(d))
