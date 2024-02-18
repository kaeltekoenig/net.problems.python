# Стоимость абонементов и билетов
one = 15
five = 70
ten = 125
twenty = 230
sixty = 440

# Вводим кол-во поездок
rides = int(input('Введите количество поездок: '))

# Раскладываем по абонементам
ticket_60 = rides // 60
ticket_20 = (rides % 60) // 20
ticket_10 = ((rides % 60) % 20) // 10
ticket_5 = (((rides % 60) % 20) % 10) // 5
ticket_1 = (((rides % 60) % 20) % 10) % 5


# # Первый вывод
# print(
# f'Абонементов на 60 поездок: {ticket_60}\n'.rjust(41),
# f'Абонементов на 20 поездок: {ticket_20}\n'.rjust(40),
# f'Абонементов на 10 поездок: {ticket_10}\n'.rjust(40),
# f'Абонементов на 5 поездок: {ticket_5}\n'.rjust(40),
# f'Обычных билетов: {ticket_1}\n'.rjust(40)
# )

# Оптимизируем по выгоде
if ticket_20 * twenty > sixty:
    ticket_60 += ticket_20 * twenty // sixty
    ticket_20 -= ticket_20 * twenty // sixty

if ticket_10 * ten > twenty:
    ticket_20 += ticket_10 * ten // twenty
    ticket_10 -= ticket_10 * ten // twenty

if ticket_5 * five > ten:
    ticket_10 += ticket_5 * five // ten
    ticket_5 -= ticket_5 * five // ten

if ticket_1 * one > five:
    ticket_5 += ticket_1 * one // five
    ticket_1 -= ticket_1 * one // five

# Финальный вывод
print()
print(
f'Абонементов на 60 поездок: {ticket_60}\n'.rjust(41),
f'Абонементов на 20 поездок: {ticket_20}\n'.rjust(40),
f'Абонементов на 10 поездок: {ticket_10}\n'.rjust(40),
f'Абонементов на 5 поездок: {ticket_5}\n'.rjust(40),
f'Обычных билетов: {ticket_1}\n'.rjust(40)
)

print()
# Сухой вывод
print(
    ticket_1,
    ticket_5,
    ticket_10,
    ticket_20,
    ticket_60,
)