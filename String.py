#  задание №1
a = 'Hello'
b = 'World'
print(a, b)

# задание №2
print('HeLLo WORLd'.lower())

# задание №3
s = 'hello world'
print(s.capitalize())

# задание № 4
s = '       hello world      '
print(s.strip())

# задание №5
s = 'h23ev9l=7lero[] fnwwqopfrfilxpd]e'
print(s.replace('h23ev9l=7lero[] fnwwqopfrfilxpd]e', 'hello world'))

# задание №6
a = 'hello world'
for i in a:
    print(i)

# задание №7
s = 'HeLlOwOrLd'
print(s.swapcase())

print(s)

# задание №8 (измененное решение)
a = 'h23ev9l=7lero[] fnwwqopfrfilxpd]e'
print(a[0:-1:3])

# задание №9
s = 'jkds8esfie9sdfljsdl1'
print(s.isalnum())

# задание №10
b = '92a38402830n948'
print(s.isalnum())

# задание № 11
a = 'Hello '
print(a * 3)

# задание № 12
s = 'HeLlOwOrLd'
b = ''
for i in s:
    if i.islower():
        b += i.upper()
    else:
        b += i.lower()
print(b)

dsk