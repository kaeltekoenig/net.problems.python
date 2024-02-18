number = int(input())

units = number % 10
digits = number % 100 // 10
hundreds = number % 1000 // 100
thousands = number // 1000

if units == 1:
    units = 'I'
elif units == 2:
    units = 'I' * 2
elif units == 3:
    units = 'I' * 3
elif units == 4:
    units = 'I' + 'V'
elif units == 5:
    units = 'V'
elif units == 6:
    units = 'V' + 'I'
elif units == 7:
    units = 'V' + 'I' * 2
elif units == 8:
    units = 'V' + 'I' * 3
elif units == 9:
    units = 'I' + 'X'


if digits == 1:
    digits = 'X'
elif digits == 2:
    digits = 'X' * 2
elif digits == 3:
    digits = 'X' * 3
elif digits == 4:
    digits = 'X' + 'V'
elif digits == 5:
    digits = 'L'
elif digits == 6:
    digits = 'L' + 'X'
elif digits == 7:
    digits = 'L' + 'X' * 2
elif digits == 8:
    digits = 'L' + 'X' * 3
elif digits == 9:
    digits = 'X' + 'C'
    
if hundreds == 1:
    hundreds = 'C'
elif hundreds == 2:
    hundreds = 'C' * 2
elif hundreds == 3:
    hundreds = 'C' * 3
elif hundreds == 4:
    hundreds = 'C' + 'D'
elif hundreds == 5:
    hundreds = 'D'
elif hundreds == 6:
    hundreds = 'D' + 'C'
elif hundreds == 7:
    hundreds = 'D' + 'C' * 2
elif hundreds == 8:
    hundreds = 'D' + 'C' * 3
elif hundreds == 9:
    hundreds = 'C' + 'M'

if thousands == 1:
    thousands = 'M'
elif thousands == 2:
    thousands = 'M' * 2
elif thousands == 3:
    thousands = 'M' * 3
else:
    thousands = ''


print(thousands, hundreds, digits, units, sep ='')