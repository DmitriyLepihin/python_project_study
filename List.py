# задание № 1
a = [1, 2, 3, 4]
print(a)

# задание № 2 (нет 10 элемента)
a = [1, 2, 3, 4, 5, 6, 7]
print(a[0], a[3])

# задание № 3
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(a[2:-1:2])

# задание № 4
a = [1, 2, 3, 4, 5, 6, 7]
a.append('a')
print(a)

# задание № 5
a = [1, 2, 3, 4, 5, 6, 7]
a.insert(0, 'b')
print(a)

# задание № 6
a = [1, 2, 3, 4, 5, 6, 7]
b = ['a', 'b', 'c']
print(a + b)

# задание № 7
a = [1, 2, 3, 4, 5, 6, 7]
a.reverse()
print(a)

# задание № 8
a = [1, 2, 3, 8, 4, 5, 8, 6, 8, 7]
cnt = 0
for i in range(len(a)):
    if a[i] == 8:
        cnt += 1
print(cnt)

# задание № 9
a = ['H', 'e', 'l', 'l', 'o']
for i in range(len(a)):
    c = ''
    if a[-1] != a[i]:
        c += a[i]
        print(c, end='+')
    else:
        c += a[-1]
        print(c, end='')
print()

# задание № 10
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
a.insert(2, b)
print(a)

# задание № 11
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
a[2] = b
print(a)

# задание № 12
a = [1, 2, 3, 4, 5]
b = a
