f = open('input.txt')
s = f.readline().rstrip()
o = open('output.txt', 'w')
o.write(s[::-1])