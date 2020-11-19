# задание № 1
a = [1, 2, 3, 4, 5, 6]
for i in a:
    if i % 2 == 0:
        print(i)
        break

# задание № 2
a = [1, 'a', [1, 2, 3], {1: 2}, (1, 2, 3,), {'a': 'old key'}]
for elem in a:
    if type(elem) == dict:
        elem.update({'a': 'new key'})
print(a)

# задание № 2 (второй варинат решения)
a = [1, 'a', [1, 2, 3], {1: 2}, (1, 2, 3,), {'a': 'old key'}]
for elem in a:
    if isinstance(elem, dict):
        elem.update({'a': 'new key'})
print(a)

# задание № 3
b = input()
c = '123456789'
d = len(b)
f = ''
if len(b) > 9:
    print(b[-9::])
if len(b) < 9:
    for i in range(len(c) - len(b)):
        d += 1
        f += (str(d))
    f = ' '.join(f)
    print(b + f)

# задание № 4
a = 89
if a > 89:
    print('bigger')
if a == 89:
    print('equal')
if a < 89:
    print('less')

# задание 5
a = 'skdhlzx;hfkhsnkeluewrtyeruopvcwqsnewfawhrevnetrvnoesrvpser'
b = 'hello'
for letter in b:
    if letter in a:
        b = b.replace(letter, '')
if len(b) == 0:
    print('It is possible to form a word')
else:
    print('It is impossible to form a word')

# задача № 6
a = 'some'
b = '99999999999999Some9999999'
b = b.lower()
if a in b:
    print(b.replace('some', 'HouSe'))
else:
    print('Variable not found')

# задание 7
a = 'dkfjoiewjvoelistsfjskdejf'
if 'list' in a:
    a = a.split()
if 'set' in a:
    a = set(a)
if 'tuple' in a:
    a = tuple(a)
print(a, type(a))
