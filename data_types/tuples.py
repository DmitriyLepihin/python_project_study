# задание № 1
a = 'Test string'  # можно a = tuple('Test string')
b = tuple(a)
print(b)
a = 'Test string'  # вариант решения циклом только такой, tuple == неизменяемый тип
b = []
for i in a:
    b.append(i)
c = tuple(b)
print(c, type(c))
# задание № 2
a = [1, 2, 3, 4]  # можно a = tuple([1, 2, 3, 4])
b = tuple(a)
print(b, type(b))
a = [1, 2, 3, 4]  # вариант решения циклом только такой, tuple == неизменяемый тип
b = []
for i in a:
    b.append(i)
c = tuple(b)
print(c, type(c))
# задание № 3
t = {1: 2, 3: 4, 5: 6}
b = tuple(t)
print(b, type(b))
t = {1: 2, 3: 4, 5: 6}
b = []
for i in t.keys():
    b.append(i)
c = tuple(b)
print(c, type(c))
# задание № 4 нельзя сделать конкатенацию строки и кортежа, только tuple + tuple
a = ('2', 33, 4,)
b = 'a'
c = tuple(b)
print(a + c)
