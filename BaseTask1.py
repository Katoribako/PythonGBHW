# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать
# формулу:(выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.

from sys import argv

name_script, production, rate, award = argv
production = int(production)
rate = int(rate)
award = int(award)
print(f"Production is {production}")
print(f"Rate is {rate}")
print(f"Award is {award}")
print(f"Your solary is {(production * rate) + award}")
