from datetime import datetime
from os import path


# задание № 1
def greetings(n):
    word = 'privet'
    if n == 0:
        return
    for i in range(n):
        print(word)


# задание № 1 (второй варинат)
def greetings2(n):
    word = 'privet'
    if n == 0:
        return
    while n > 0:
        print(word)
        n -= 1


# задание № 1 (третий вариант)
def rec_greetings(n):
    if n == 0:
        return
    if n > 0:
        n -= 1
        print('privet')
        rec_greetings(n)


# задание № 2
def draws(n):
    a = '+'
    middle = (n - 1) / 2 + 1
    count = 1
    for i in range(n + 1):
        if i < middle - 1:
            picture = a * count
            print(picture.center(n * 2))
            count += 2
        if i == middle:
            picture = a * n
            print(picture.center(n * 2))
        if i > middle:
            count -= 2
            picture = a * count
            print(picture.center(n * 2))


# задание № 3
def word_search(set_of_letters, word):
    for letter in word:
        if letter in set_of_letters:
            word = word.replace(letter, '')
    if len(word) == 0:
        return True
    else:
        return False


# задание № 4
def create_dict(n):
    my_dict = {}
    count = 0
    for letter in n:
        count += 1
        if count == 3:
            my_dict[letter] = my_dict.setdefault(letter)
            count = 0
    return my_dict


# задание № 4 (второй вариант)
def create_dict2(n):
    dicts = dict.fromkeys(n[2::3])  # подумал, что это будет лучше - не прогоняем цикл и ничего не добавляем в список
    return dicts  # а сразу работаем с поданной строкой


# задание № 5
def times():
    n = datetime.now()
    return n


# задание № 6
def day_of_week():
    n = datetime.today().strftime('%A')
    return n


# задание № 7
def remind():
    n = datetime.today().strftime('%A')
    if n == 'Wednesday' or n == 'Friday':
        return ('Go to sport')
    else:
        return ('Without sports today')


# задание 8
def define_methods(n):
    return dir(n)


# задание 9
def addition(n):
    n += 13
    return str(n)


# задание 10
def trim_add(n):
    if len(n) > 7:
        return n[:7]
    if len(n) < 7:
        while len(n) <= 7:
            n += n
        return n[:7]


# задание 11
def create_str(n):
    for i in range(len(n)):
        if type(n[i]) == int:
            n[i] = str(n[i])
    return ''.join(n)


# задание 12
def create_file(n):
    if type(n) == int:
        with open(addition(n), 'a') as file:
            file.write('Done!')
    if type(n) == str:
        with open(trim_add(n), 'a') as file:
            file.write('Done!')
    if type(n) == list:
        with open(create_str(n), 'a') as file:
            file.write('Done!')


# задание 13
def creating_numbered_files(n):
    for i in range(1, n + 1):
        with open(f'new_file_{i}.txt', 'a') as file:
            file.write('')


# задание № 14
def check_create(n):
    for i in range(1, n + 1):
        if path.isfile(f'new_file_{i}.txt'):
            print(f'new_file_{i}.txt', 'File exists')
        else:
            with open(f'new_file_{i}.txt', 'a') as file:
                file.write('')
                print(f'new_file_{i}.txt', 'Create new file')


greetings(25)
greetings2(25)
rec_greetings(25)
draws(7)
print(word_search('skdhlzx;hfkhsnkeluewritymeruopvacwqsnewfawhrevnetrvnoesrvpser', 'hello'))
print(create_dict2('fhsefisdvdsufbsdkbvjhsdfbvshdbv'))
print(create_dict('fhsefisdvdsufbsdkbvjhsdfbvshdbv'))
print(times())
print(day_of_week())
print(remind())
d = [1, 2, 3, 4]
print(define_methods(d))
number = 0
string_number = addition(number)
print(string_number, type(string_number))
string = 'wert'
new_string_seven = trim_add(string)
print(new_string_seven)
lists = ['sdjvb', 4, 'sldj', 237]
new_str_lists = create_str(lists)
print(new_str_lists)
create_file(0)
create_file('dima')
create_file([26, 5, 1991, 'Dima'])
creating_numbered_files(5)
check_create(7)
