# Узник замка Иф
# За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D×E. 
# Замок Иф сложен из кирпичей, размером A×B×C. Определите, сможет ли узник выбрасывать кирпичи 
# в море через это отверстие, если стороны кирпича должны быть параллельны сторонам отверстия.

# Программа получает на вход числа A, B, C, D, E и должна вывести слово YES или NO.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

# Теперь а - минимальное ребро, б - среднее, c - не учитываем, берем ее как длину, 
# а в отверстие можно просунуть кирпич любой длины 
    
if d > e:
    d, e = e, d
    
# d - миним. отверстие, e - максим. отверстие
    
if a <= d and b <= e:
    print('YES')
else:
    print('NO')