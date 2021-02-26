from datetime import datetime
from os import path


def writing_to_file(n):
    with open(n, 'w') as file:
        file.write('Done!')


# задание № 1
# создать функцию которая распечатает n раз слово privet - n передается как параметр функции
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
# создать функцию которая рисует
#    +
#   +++
#  +++++
#   +++
#    +
# размер ромба задается через параметр функции
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
# сделать функцию в которую передается строка “skdhlzx;hfkhsnkeluewrtyeruopvcwqsnewfawhrevnetrvnoesrvpser” и
# шаблон слова, внутри функции опреелять  возможно ли собрать из букв,что в ней находятся переанное слово для сборки,
# результат лио True либо False?
def word_search(set_of_letters, word):
    for letter in word:
        if letter in set_of_letters:
            word = word.replace(letter, '')
    if len(word) == 0:
        return True
    else:
        return False


# задание № 4
# есть функция на вход подается строка ‘fhsefisdvdsufbsdkbvjhsdfbvshdbv’ фнутри функции из строки достается каждый 3
# символ и делается ключем словаря и созданный словарь возвращается из функции - распечатать полученный словарь
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
# функция которая отдает текущее время
def times():
    n = datetime.now()
    return n


# задание № 6
# функция которая отдает текущий день недели
def day_of_week():
    n = datetime.today().strftime('%A')
    return n


# задание № 7
# функция которая если  сегодня среда и пятница отдает сообщение “go to sport”
def remind():
    n = datetime.today().strftime('%A')
    if n == 'Wednesday' or n == 'Friday':
        return ('Go to sport')
    else:
        return ('Without sports today')


# задание 8
# функция которая на вход параметром получает некий тип (не важно инт стринг лист), а функция печатает магические
# методы этого тиго типа
def define_methods(n):
    return dir(n)


# задание 9
# функция которая на вход получает некое число и плюсует к нему 13 и возвращает результат в виде строки
def addition(n):
    n += 13
    return str(n)


# задание 10
# функция которая на вход получает некую строку и обрезает ее до 7 букв или увеличивает до 7 букв из тех что есть и
# возвращает результат
def trim_add(n):
    if len(n) > 7:
        return n[:7]
    if len(n) < 7:
        n *= 7
        return n[:7]


# задание 11
# функция которая на вход получает некий список(из строковых элементов или числовых или то и то) и склеивает все
# элементы в строку и возвращает результат
def create_str(n):
    for i in range(len(n)):
        if type(n[i]) == int:
            n[i] = str(n[i])
    return ''.join(n)


# задание 12
# функция куда на вход подается либо строка, либо число, либо список(состоящий из строковых
# элементов или чисел или того и того) - то бишь на вход три параметра, задача выяснить какой из параметров передан
# не пустым, и используя функции из этого блока из заданий 9,10,11 получить строку из переданного элемента,
# а затем создать файл со строкой “Done!” и сохранить в файл имя которого взято из результата работы функции
# примененной к этому типу данных полученных на вход в функцию. к примеру: на вход подаем строку “wert” на выходе
# функция создает файл с названием wertwer и в нем слово Done записано. на вход подаем 67 на выходе функция создает
# файл с названием 80 и текстом Done
def create_file(n):
    if type(n) == int:
        writing_to_file(addition(n))
    if type(n) == str:
        writing_to_file(trim_add(n))
    if type(n) == list:
        writing_to_file(create_str(n))


# задание 13
# функция которая создает файлы - их количество равно числу переданному через параметр функции, называть
# файлы new_file_{num}.txt где num - номер созданного файла
def creating_numbered_files(n):
    for i in range(1, n + 1):
        with open(f'new_file_{i}.txt', 'w') as file:
            file.write('')


# задание № 14
# функция которая проверяет все ли файлы созданы, файлы в папке называются по след шаблону new_file_{num}.txt
# (либо результат работы пред функции) если у меня передано в функцию число 7 а в папке лежат
# файлы new_file_0.txt new_file_5.txt new_file_6.txt - то мне необходимо создать файлы под номером 1,2,3,4,7,
# вообщем все недостающие, если все ок - сказать - все файлы в наличии, либо напечатать имена файлов что созданы
def check_create(n):
    for i in range(1, n + 1):
        if path.isfile(f'new_file_{i}.txt'):
            print(f'new_file_{i}.txt', 'File exists')
        else:
            with open(f'new_file_{i}.txt', 'w') as file:
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
