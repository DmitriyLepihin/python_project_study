# задача № 1
# cделать из строки “Test string” кортеж ('T', 'e', 's', 't', ' ', 's', 't', 'r', 'i', 'n', 'g') (и циклом тоже)
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
# сделать из списка a = [1,2,3,4] кортеж (1,2,3,4)
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
# из словаря t = {1:2, 3:4, 5:6} сделать кортеж (1,3,5) (и циклом тоже)
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
# есть кортеж a = ('2',’33’, ‘4’,)  добавить к нему b = ‘a’
a = ('2', 33, 4,)
b = 'a'
c = tuple(b)
print(a + c)
