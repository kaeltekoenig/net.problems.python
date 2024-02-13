text = input()

def reverse_sec_word(txt):
    if txt.find(' ') == -1:
        return f'*{txt}*'
    elif txt.find(' ', txt.find(' ')+1) == -1:
        second_word = txt[txt.find(' ')+1:]
        print(second_word)
        return f'*{txt[:txt.find(' ')]} {second_word[::-1]}*'
    else:
        first_word = txt[:txt.find(' ')]
        second_word = txt[txt.find(' ')+1:txt.find(' ', txt.find(' ')+1)]
        rest = txt[txt.find(' ', txt.find(' ')+1)+1:]
        return f'*{first_word} {second_word[::-1]} {rest}*'


print(
    reverse_sec_word(text)
)