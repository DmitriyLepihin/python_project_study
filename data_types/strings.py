#  задание №1
# сложить две строки ‘Hello’, ‘World’ -> ‘Hello World’
a = 'Hello'
b = 'World'
print(a, b)

# задание №2
# сделать из строки ‘HeLLo WORLd’ -> ‘hello world’
print('HeLLo WORLd'.lower())

# задание №3
# сделать из строки ‘hello world’ -> ‘Hello world’
s = 'hello world'
print(s.capitalize())

# задание № 4
# сделать из строки ‘      hello world      ’ -> ‘hello world’
s = '       hello world      '
print(s.strip())

# задание №5
# сделать из строки 'h23ev9l=7lero[] fnwwqopfrfilxpd]e' -> 'hello world'
s = 'h23ev9l=7lero[] fnwwqopfrfilxpd]e'
print(s.replace('h23ev9l=7lero[] fnwwqopfrfilxpd]e', 'hello world'))

# задание №6
# распечать в консоль по буквам строку ‘hello world’
a = 'hello world'
for i in a:
    print(i)

# задание №7
# сделать из строки ‘HeLlOwOrLd’ -> hElLoWoRlD - решить методом
s = 'HeLlOwOrLd'
print(s.swapcase())

print(s)

# задание №8 (измененное решение)
# посчитать сколько букв ‘e’ в строке a = 'h23ev9l=7lero[] fnwwqopfrfilxpd]e'
a = 'h23ev9l=7lero[] fnwwqopfrfilxpd]e'
print(a[0:-1:3])

# задание №9
# узнать есть ли в строке числа a = ‘jkds8esfie9sdfljsdl1’
s = 'jkds8esfie9sdfljsdl1'
print(s.isalnum())

# задание №10
# узнать есть ли в строке буквы a = ‘92a38402830n948’
b = '92a38402830n948'
print(s.isalnum())

# задание № 11
# сделать из строк ‘Hello ’ строку 'Hello Hello Hello '
a = 'Hello '
print(a * 3)

# задание № 12
# сделать из строки ‘HeLlOwOrLd’ -> hElLoWoRlD - решить циклом
s = 'HeLlOwOrLd'
b = ''
for i in s:
    if i.islower():
        b += i.upper()
    else:
        b += i.lower()
print(b)
