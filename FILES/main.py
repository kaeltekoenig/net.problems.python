# ЧТЕНИЕ ПОСТРОЧНО
f = open('aint.in')            # по умолчанию режим read
a = f.readline().rstrip()   # в обычном формате в строку записывается \n
b = f.readline().rstrip()
o = open('aint.out', 'w')
o.write(str(a + b))
f.close()
o.close()

# # ЧТЕНИЕ ПОБАЙТОВО (ПОСИМВОЛЬНО)
# f = open('a.in')
# s = f.read(1)
# while s:
#     print('<<' + s + '>>')
#     s = f.read(1)


# СОЗДАНИЕ СПИСКА СТРОК
f = open('astr.in')
s = list(map(lambda x: str(x).rstrip(), f.readlines()))
# print(s)              # ['Hello\n', 'World\n', 'my\n', 'friend'] ----- Просто f.readlines()
o = open('astr.out', 'w')
o.write(' '.join(s))             # необходимо явно преобразовать в str
f.close()
o.close()