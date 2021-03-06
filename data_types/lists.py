# задание № 1
# создать список a = [1,2,3,4]
a = [1, 2, 3, 4]  # это уже список
print(a)

# задание № 2 (10эл. вытащить нельзя, обращение при вытягивание к несуществующему индексу == ошибка )
# есть список a = [1,2,3,4,5,6,7] достать из него 0, 3 и 10 элемент
a = [1, 2, 3, 4, 5, 6, 7]
print(a[0], a[3])

# задание № 3
# есть список a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] достать каждый 3 элемент списка начиная со 2-го элемента
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(a[2::3])  # наконец-то исправил

# задание № 4
# есть список a = [1,2,3,4,5,6,7] добавить в его конец новое значение “a”
a = [1, 2, 3, 4, 5, 6, 7]
a.append('a')
print(a)

# задание № 5
# есть список a = [1,2,3,4,5,6,7] добавить в его начало новое значение “a”
a = [1, 2, 3, 4, 5, 6, 7]
a.insert(0, 'b')
print(a)

# задание № 6
# есть список a = [1,2,3,4,5,6,7] и список b = [“a”, “b”, “c”] сделать из них один список [1,2,3,4,5,6,7, “a”, “b”, “c”]
a = [1, 2, 3, 4, 5, 6, 7]
b = ['a', 'b', 'c']
print(a + b)
a.extend(b)  # тот самый метод
print(a)

# задание № 7
# есть список a = [1,2,3,4,5,6,7] сделать из него [7,6,5,4,3,2,1]
a = [1, 2, 3, 4, 5, 6, 7]
a.reverse()
print(a)
print(a[::-1])  # в данном случае выдаст снова первоначальный список, т.к. использовали метод reverse()

# задание № 8
# есть список a = [1,2,3,8,4,5,8,6,8,7]  - подсчитать сколько в списке цифр 8
a = [1, 2, 3, 8, 4, 5, 8, 6, 8, 7]
cnt = 0
for i in range(len(a)):
    if a[i] == 8:
        cnt += 1
print(cnt)
print(a.count(8))  # метод возращает количество нужного элемента в списке

# задание № 9
# сделать из списка a = [‘H’, ‘e’, ‘l’, ‘l’, ‘o’] строку “H+e+l+l+o”
a = ['H', 'e', 'l', 'l', 'o']
a = '+'.join(a)
print(a, type(a))

# задание № 10
# есть список a = [1,2,3,4,5] и b = [‘a’,’b’,’c’]. Список b вставить в список a на 2 позицию.
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
a.insert(2, b)
print(a)

# задание № 11
# есть список a = [1,2,3,4,5] и b = [‘a’,’b’,’c’]. Список b вставить в список a вместо 2 позиции.
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
a[2] = b
print(a)

# задание № 12
# вставить в список a список b вместо 2 позиции, чтобы получилось [1,2,[1,2,3,4,5],4,5]
# a = [1,2,3,4,5], b = a
a = [1, 2, 3, 4, 5]
b = a.copy()  # как вариант b = a[::] - тоже копия
a[2] = b
print(a)
