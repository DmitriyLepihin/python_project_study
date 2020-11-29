# задание № 1 (циклом for)

word = 'привет'
for i in range(1000):
    print(word)

# задание № 1 (циклом while)
word = 'привет'
count = 0
while count < 1000:
    print(word)
    count += 1

# задание № 2
numbers = 122693294659027459834
numbers_2 = str(numbers)
lists_numbers = []
for i in numbers_2:
    if int(i) % 3 == 0:
        lists_numbers.append(int(i))
print(lists_numbers)

# задание № 3
a = [1, [1, 2, 3], 'a', {1: 1}, [5, 6], 9, 'b']
b = []
for elem in a:
    if type(elem) == int:
        b.append(elem)
        a.remove(elem)
    if elem == str:
        b.append(elem)
        a.remove(elem)
for elem in a:
    if type(elem) == str:
        b.append(elem)
        a.remove(elem)
for elem in a:
    if type(elem) == list:
        b.append(elem)
        a.remove(elem)
for elem in a:
    if type(elem) == dict:
        b.append(elem)
print(b)

# задание № 3 (второй вариант)
INDEX_INT = 0
a = [1, [1, 2, 3], 'a', {1: 1}, [5, 6], 9, 'b']
b = []
count_int = 0
count_str = 0
count_list = 0
for elem in a:
    if type(elem) == int:
        b.insert(INDEX_INT, elem)
        count_int += 1
        print()
    if type(elem) == str:
        b.insert(count_int, elem)
        count_str = count_int + 1
        print()
    if type(elem) == list:
        if count_int == 0:
            count_list = count_int
            b.insert(count_list, elem)
            continue
        if count_str == 0 and count_list == 0:
            count_list = count_int
        elif count_str == 0:
            count_list = count_int + 1
        else:
            count_list = count_str + 1
        b.insert(count_list, elem)
        print()
    if type(elem) == dict:
        b.append(elem)
        print()
print(b)

# задание № 4
a = {'fruit': {'banan': {'price': 100, 'count': 1}}, 'vegitable': {'potato': {'price': 78, 'count': 3}}}
profit = 0
for key in a.keys():
    for value in a[key].values():
        profit += value['price'] * value['count']
print(profit)

# задание № 5
a = 20
while a <= 31:
    a += 0.392
print(a)

# задание № 6
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
for i in a:
    for j in i:
        if j % 3 == 0:
            i.remove(j)
print(a)

# задание № 7
a = [1, 10, 100]
b = []
while a[0] <= 3:
    a[0] += 0.546
    if a[0] >= 3:
        b.append(a[0])
while a[1] <= 30:
    a[1] += 0.546
    if a[1] >= 30:
        b.append(a[1])
while a[2] <= 300:
    a[2] += 0.546
    if a[2] >= 300:
        b.append(a[2])
print(b)

# задание №7 (второй вариант)
a = [1, 10, 100]
for elem in range(len(a)):
    check_number = a[elem] * 3
    while a[elem] <= check_number:
        a[elem] += 0.546
        if a[elem] >= check_number:
            break
print(a)

# задание № 8
a = [1, 10, 100]
for i in range(len(a)):
    n = a[i] * 3 // 0.546
    a[i] += 0.546 * n
print(a)

# задание № 9
a = '+'
size = 5
middle = (size - 1) / 2 + 1
count = 1
for i in range(size + 1):
    if i < middle - 1:
        picture = a * count
        print(picture.center(size * 2))
        count += 2
    if i == middle:
        picture = a * size
        print(picture.center(size * 2))
    if i > middle:
        count -= 2
        picture = a * count
        print(picture.center(size * 2))