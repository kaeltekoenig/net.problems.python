import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
i = 0
books = []

while i < len(lst_in):
    if ' ' not in lst_in[i]:
        books.append(lst_in[i])
    i += 1

print(*books)