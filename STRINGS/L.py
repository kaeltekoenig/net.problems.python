text = input()

teams, space, score = text.rpartition(' ')
a_team, hyphen, b_team = teams.partition('-')
a_score, colons, b_score = score.partition(':')

if a_score > b_score:
    print('*' + a_team + '*')
elif a_score < b_score:
    print('*' + b_team + '*')
else:
    print('draw')
