# задание № 1
a = [1, 2, 3, 4]  # это уже список
print(a)

# задание № 2 (10эл.  вытащить нельзя, обращение при вытягивание к несуществующему индексу == ошибка )
a = [1, 2, 3, 4, 5, 6, 7]
print(a[0], a[3])

# задание № 3
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(a[2:-1:3])

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
a.extend(b) # тот самый метод
print(a)

# задание № 7
a = [1, 2, 3, 4, 5, 6, 7]
a.reverse()
print(a)
print(a[::-1]) # в данном случае выдаст снова первоначальный список, т.к. использовали метод reverse()

# задание № 8
a = [1, 2, 3, 8, 4, 5, 8, 6, 8, 7]
cnt = 0
for i in range(len(a)):
    if a[i] == 8:
        cnt += 1
print(cnt)
print(a.count(8)) # метод возращает количество нужного элемента в списке

# задание № 9
a = ['H', 'e', 'l', 'l', 'o']
a = ''.join(a)
print(a, type(a))

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
b = a.copy()  # как вариант b = a[::] - тоже копия
a[2] = b
print(a)