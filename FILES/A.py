fin = open('input.txt')
a = int(fin.readline())
b = int(fin.readline())
out = open('output.txt', 'w')
out.write(str(a + b))
fin.close
out.close()