from datetime import datetime


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
