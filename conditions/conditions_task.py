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

# второй варинат решения задачи
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
    print(b)

# задание № 4
a = 89
if a > 89:
    print('bigger')
if a == 89:
    print('less')
if a < 89:
    print('equal')

# задание 5  супер-говно :( но выводит все как надо
# конечно можно обмануть всех -> b = a.replace( 'hello') но этот метод не для этого
a = 'skdhlzx;hfkhsnkeluewrtyeruopvcwqsnewfawhrevnetrvnoesrvpser'
b = ''
for i in a:
    if i == 'h' or i == 'e':
        b += i
    if i == 'l' or i == 'o':
        b += i
print(b.count('h'), b.count('e'), b.count('l'), b.count('o'))
c = b.replace('h', '', 3).replace('e', '', 7).replace('o', '', 1)
letter_one = ''
letter_two = ''
leter_three = ''
leter_four = ''
for j in c:
    if j == 'h':
        letter_one += j
    if j == 'e':
        letter_two += j
    if j == 'l':
        leter_three += j
    if j == 'o':
        leter_four += j
word = letter_one + letter_two + leter_three + leter_four
print(word)
