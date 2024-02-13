# Текст состоит из слов, разделённых пробелами. В тексте как минимум три слова. 
# Удалите из текста второе слово.

# Решение выведите так же, как в задаче «Две половинки».

# В этой задаче нельзя использовать методы count и replace. 
# Также желательно использовать метод find с двумя параметрами, вместо вызова метода find к срезу.

text = 'In the hole in the ground there lived a hobbit'


first_space_i = text.find(' ')
first_word = text[:first_space_i]
rest = text[first_space_i + 1:]

second_space_i = rest.find(' ')
rest_b = rest[second_space_i:]

new_text = first_word + rest_b
print(f'*{new_text}*')