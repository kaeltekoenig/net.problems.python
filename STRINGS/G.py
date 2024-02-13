# Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами.
# При решении этой задачи нельзя пользоваться циклами и инструкцией if.
text = 'Hello world'

separator_index = text.find(' ')
first_word = text[:separator_index]
second_word = text[(separator_index + 1):]

print('*' + second_word, first_word + '*')
# *world Hello*