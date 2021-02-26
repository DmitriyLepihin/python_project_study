# задание № 1

a = [1, 2, 3, 4, 5, 6]
for i in a:
    if i % 2 == 0:
        print(i)
        break

# задание № 2
# есть список a = [1, ‘a’, [1,2,3], {1:2}, (1,2,3,), {“a”:”old key”}] найти в списке элементы которые являются
# словарем и добавить в них новый ключ “a”: “new key”
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
# на ввод с консоли подаем произвольную строку, смотрим эта строка больше 9 символов, если да, обрезаем ее на 9
# символов с конца и выводим, если нет, докидываем недостающее количество символов числами по порядку через пробел
# “shdfjask123456789” -> “123456789”
# “sdf” - > “sdf4 5 6 7 8 9”
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
# a = 89 если a > 89 вывести bigger, если меньше вывести less если равно вывести equal
a = 89
if a > 89:
    print('bigger')
if a == 89:
    print('equal')
if a < 89:
    print('less')

# задание 5
# есть строка “skdhlzx;hfkhsnkeluewrtyeruopvcwqsnewfawhrevnetrvnoesrvpser” возможно ли собрать из букв,что в ней
# находятся слово hello?
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
# есть переменная a = “some” и строка b = “99999999999999Some9999999” есть ли a в b (независимо от регистра букв),
# если есть заменить some на HouSe
a = 'some'
b = '99999999999999Some9999999'
b = b.lower()
if a in b:
    print(b.replace('some', 'HouSe'))
else:
    print('Variable not found')

# задание 7
# есть строка a = “dkfjoiewjvoelistsfjskdejf” есть ли в ней слово list, если есть - сделать из строки a - list,
# если есть в строке a слово set сделать из строки сет, если есть в строка a слово tuple - сделать из строки tuple
a = 'dkfjoiewjvoelistsfjskdejf'
if 'list' in a:
    a = a.split()
if 'set' in a:
    a = set(a)
if 'tuple' in a:
    a = tuple(a)
print(a, type(a))

# задание № 8
# a = [{“2”:[1,2,,4,5]}, “dima”, list(“1,2,3,4”), 3, 2] есть ли элемент списка кратный двум, если да, то вывести его
a = [{'2': [1, 2, 4, 5]}, 'dima', list('1,2,3,4'), 3, 2]
for elem in a:
    if type(elem) == int and elem % 2 == 0:
        print(elem)

# задание № 9 подбил все буквы вне зависимости повторяются они или нет.
a = 'asadsfjsdfusehfuishezvblkaufhsdnvsidnuseuesfhd'
vowels = 0
consonants = 0
for letter in a:
    if letter in 'aeiouy':
        vowels += 1
    else:
        consonants += 1
print(vowels, consonants)

# 9 второй варинат решения (только буквы которые не повторяются)
# a = “asadsfjsdfusehfuishezvblkaufhsdnvsidnuseuesfhd” - посчитать количество гласных и согласных в строке и вывести
# информацию в консоль
a = 'asadsfjsdfusehfuishezvblkaufhsdnvsidnuseuesfhd'
my_set_a = set(a)
vowels = 0
consonants = 0
for letter in my_set_a:
    if letter in 'aeiouy':
        vowels += 1
    else:
        consonants += 1
print(vowels, consonants)

# задание 10. подбил все цифры вне зависимости повторяются они или нет
# a = “39846789857394845793857193874593485” узнать сколько числе делиться на два без остатка, и на три и вывести
a = '39846789857394845793857193874593485'
summ_numbers_2 = 0
summ_numbers_3 = 0
for i in a:
    if int(i) % 2 == 0:
        summ_numbers_2 += 1
    if int(i) % 3 == 0:
        summ_numbers_3 += 1
print(summ_numbers_2, summ_numbers_3)

# задание № 10. второй варинат решения подбил все без повторов.
a = '39846789857394845793857193874593485'
summ_numbers_2 = set()
summ_numbers_3 = set()
for i in a:
    if int(i) % 2 == 0:
        summ_numbers_2.add(i)
    if int(i) % 3 == 0:
        summ_numbers_3.add(i)

summ_numbers_2 = len(summ_numbers_2)
summ_numbers_3 = len(summ_numbers_3)
print(summ_numbers_2, summ_numbers_3)
