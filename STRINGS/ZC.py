text = input()


NS = 0
WE = 0

for elem in text:
    if elem.isalpha():
        if elem == 'N':
            NS += int(text[:text.find(elem)])
        elif elem == 'S':
            NS -= int(text[:text.find(elem)])
        elif elem == 'W':
            WE += int(text[:text.find(elem)])
        elif elem == 'E':
            WE -= int(text[:text.find(elem)])
        text = text[text.find(elem)+1:]

if NS > 0:
    NS_str = f'{NS}N'
elif NS < 0:
    NS_str = f'{abs(NS)}S'
else:
    NS_str = ''

if WE > 0:
    WE_str = f'{WE}W'
elif WE < 0:
    WE_str = f'{abs(WE)}E'
else:
    WE_str = ''


print(f'{NS_str}{WE_str}')