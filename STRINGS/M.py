text = 'Python'

def add_dot_between(strn):
    if len(strn) == 1:
        return strn + '.'
    else:
        rest = strn.partition(strn[-1])[0]
        sep = strn.partition(strn[-1])[1]
        return add_dot_between(rest) + sep + '.'
    
print('*' + add_dot_between(text).rpartition('.')[0] + '*')

