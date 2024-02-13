text = input()

for i in range(len(text)):
    new_text = text[:i] + text[i+1:]
    if new_text == new_text[::-1]:
        print(i+1)
        break
else:
    print(0)