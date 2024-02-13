text = input()

for i in range(len(text)):
    new_text = text + text[i::-1]
    if new_text == new_text[::-1]:
        break

print(len(new_text) - len(text))