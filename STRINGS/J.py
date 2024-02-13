# Повторение слова
# Текст состоит из слов, разделённых пробелами. В тексте как минимум два слова. 
# Продублируйте второе слово в тексте.

# В этой задаче нельзя использовать методы count и replace. 
# Также желательно использовать метод find с двумя параметрами, вместо вызова метода find к срезу.


text = input()

left_border = text[:text.find(' ')]
right_border = text[text.find(' ') + 1:]

if right_border.find(' ') == -1:
    second_word = right_border
else:
    second_word = right_border[:right_border.find(' ')]

result = '*' + left_border + ' ' + second_word + ' ' + right_border + '*'
print(result)

