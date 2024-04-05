months = {
    'January': 1,
    'February': 2,
    'March': 3
}

date = 'January, 1'
pos = date.find(',')

month = months[date[:pos]]
day = int(date[pos+2:])
print(month, day)


capitals = dict()
# Добавить элемент в словарь
capitals['Russia'] = 'Moscow'
capitals['Germany'] = 'Berlin'
capitals['Italy'] = 'Rome'
print(capitals)

# Удалить элемент из словаря - 1
del capitals['Russia']
print(capitals)
# Удалить элемент из словаря - 2
# capitals.pop('France')                # KeyError
capitals.pop('France', 
             'А такого и не было в словаре')    
# Второй аргумент - вернуть данное значение, если ключ не найден
print(capitals)

# Найти элемент в словаре
print(capitals.get('Germany'))          # Berlin


words = {
    'п': 0,
    'к': 0,
    'д': 0
         }

s = 'привет, как дела, привет-привет, привет, ну, але!'



# ПЕРЕБОР ЭЛЕМЕНТОВ
# по ключам
for country in capitals:
    print(f'Столица {country} - город {capitals[country]}')