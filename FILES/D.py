verse = []

f = open('input.txt')
s = f.readlines()
s[-1] = s[-1] + '\n'
s[0] = s[0].strip()

o = open('output.txt', 'w')
o.write(''.join(s[::-1]))
f.close()
o.close()