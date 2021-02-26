# задание № 1
# есть сет users = {"1","2","3",“4”} добавить в него элемент “4”
users = {'1', '2', '3', '4'}
users.add('4')  # если элемент уже присутствует во множестве, print без повтора элемента(только уникальные значения)
print(users)
# задание № 2
# есть сет users = {"1","2","3",“4”} удалить элемент “2”
users = {'1', '2', '3', '4'}
users.discard('4')
print(users)
# задание № 3
# есть сет users = {"1","2","3",“4”} добавить элемент “90”
users = {'1', '2', '3', '4'}
users.add('90')
print(users)
# задание № 4
# есть сет users = {"1","2","3",“4”} и users = {"4","1","c",“d”} найти пересечение множеств
users = {'1', '2', '3', '4'}
users_two = {'4', '1', 'c', 'd'}
users_three = users.intersection(users_two)  # либо  users & users_two
print(users_three)
# задание № 5
# есть сет users = {"1","2","3",“4”} и users = {"4","1","c",“d”} найти разницу множеств
users = {'1', '2', '3', '4'}
users_two = {'4', '1', 'c', 'd'}
users_three = users.difference(users_two)  # либо  users - users_two
print(users_three)
