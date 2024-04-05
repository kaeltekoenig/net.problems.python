languages = {}

for _ in range(int(input())):
    for __ in range(int(input())):
        lang = input()
        if lang not in languages:
            languages[lang] = 1
        else:
            languages[lang] += 1

common = []

for lan, stud in languages.items():
    if stud == len(languages):
        common.append(lan)

print(len(common))
for u in common:
    print(u)

print(len(languages))
for k in languages:
    print(k)

