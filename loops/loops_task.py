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

# задание № 4
a = {'fruit': {'banan': {'price': 100, 'count': 1}}, 'vegitable': {'potato': {'price': 78, 'count': 3}}}
basket = []
summ_profit = 0
for key in a.keys():
    for value in a[key].values():
        basket.append(value)
summ_profit = basket[0]['price'] * basket[0]['count'] + basket[1]['price'] * basket[1]['count']
print(summ_profit)

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

# задание № 8

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
