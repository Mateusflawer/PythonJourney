import calendar
import locale

locale.setlocale(locale.LC_ALL, '')

print(calendar.calendar(2024))

valor = 5445454.545


print(locale.currency(valor, grouping=True))

