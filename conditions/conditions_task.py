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

# задание 3
b = input()
if len(b) > 9:
    print(b[0:9])
if len(b) < 9:
    b += '123456789'[len(b)::]
    print(' '.join(b))

# задание № 4
a = 89
if a > 89:
    print('bigger')
if a == 89:
    print('less')
if a < 89:
    print('equal')

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
