# Скрытие адреса email

strn = 'Bilbo.Baggins@bagend.hobbiton.shire.me - valid email.'
email_address, hyphen, rest = strn.partition('-')

cyphred = email_address.replace('.', '(dot)').replace('@', '(at)')

print('*' + cyphred + hyphen + rest + '*')