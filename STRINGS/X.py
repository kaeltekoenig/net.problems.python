# Замена ребуса
# Дан ребус — таблица 5 × 5, заполненная буквами так, 
# что в каждой строке, столбце и на каждой диагонали все буквы различны.
# Нужно заменить его на другой ребус. Для этого каждая буква ребуса заменяется на другую соответствующую букву. 
# Строка для замены букв даётся сразу после ребуса.

# PS. Эта задача на maketrans и translate.


text = input()
table = text.maketrans('тилшу', 'ланчу')
print(text.translate(table))