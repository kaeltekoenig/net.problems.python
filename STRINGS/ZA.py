text = 'ABRACADABRA'
length = len(text)

for t in range(length):
    for i in range(length):
        if text[t:length+1-i] == text[t:length+1-i][::-1] and len(text[t:length+1-i]) > 2:
            palindrome = text[t:length+1-i]
            break
    else:
        continue
    break

print(f'Первый палиндром в строке: {palindrome}')