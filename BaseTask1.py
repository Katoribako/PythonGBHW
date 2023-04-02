# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.

# list version

class WrongNumber(Exception):
    pass


try:
    month_num = int(input("Please input a number of month do you like"))
    if month_num > 12 or month_num < 1:
        raise WrongNumber()
except WrongNumber:
    print("Please input correct number of mouth (It should be a integer number"
          "that >= 1 and <= 12)")
except ValueError:
    print("Please input correct number of mouth (It should be a integer number"
          "that >= 1 and <= 12)")
else:
    season_list = ['Spring', 'Summer', 'Autumn', 'Winter']
    month_dict = dict(k1='January', k2='February', k3='March', k4='April',
                      k5='May', k6='June', k7='July', k8='August',
                      k9='September', k10='October', k11='November',
                      k12='February')
    if month_num == 12 or month_num == 1 or month_num == 2:
        if month_num == 12:
            print(f"{month_dict.get('k12')} is {season_list[3]} month")
        elif month_num == 1:
            print(f"{month_dict.get('k1')} is {season_list[3]} month")
        elif month_num == 2:
            print(f"{month_dict.get('k2')} is {season_list[3]} month")
    if month_num == 3 or month_num == 4 or month_num == 5:
        if month_num == 3:
            print(f"{month_dict.get('k3')} is {season_list[0]} month")
        if month_num == 4:
            print(f"{month_dict.get('k4')} is {season_list[0]} month")
        if month_num == 5:
            print(f"{month_dict.get('k5')} is {season_list[0]} month")
    if month_num == 6 or month_num == 7 or month_num == 8:
        if month_num == 6:
            print(f"{month_dict.get('k6')} is {season_list[1]} month")
        if month_num == 7:
            print(f"{month_dict.get('k7')} is {season_list[1]} month")
        if month_num == 8:
            print(f"{month_dict.get('k8')} is {season_list[1]} month")
    if month_num == 9 or month_num == 10 or month_num == 11:
        if month_num == 9:
            print(f"{month_dict.get('k9')} is {season_list[2]} month")
        if month_num == 10:
            print(f"{month_dict.get('k10')} is {season_list[2]} month")
        if month_num == 11:
            print(f"{month_dict.get('k11')} is {season_list[2]} month")

# dict version

try:
    month_num = int(input("Please input a number of month do you like"))
    if month_num > 12 or month_num < 1:
        raise WrongNumber()
except WrongNumber:
    print("Please input correct number of mouth (It should be a integer number"
          "that >= 1 and <= 12)")
except ValueError:
    print("Please input correct number of mouth (It should be a integer number"
          "that >= 1 and <= 12)")
else:
    season_dict = dict(s1='Spring', s2='Summer', s3='Autumn', s4='Winter')
    month_dict = dict(k1='January', k2='February', k3='March', k4='April',
                      k5='May', k6='June', k7='July', k8='August',
                      k9='September', k10='October', k11='November',
                      k12='February')
    if month_num == 12 or month_num == 1 or month_num == 2:
        if month_num == 12:
            print(f"{month_dict.get('k12')} is {season_dict.get('s4')} month")
        elif month_num == 1:
            print(f"{month_dict.get('k1')} is {season_dict.get('s4')} month")
        elif month_num == 2:
            print(f"{month_dict.get('k2')} is {season_dict.get('s4')} month")
    if month_num == 3 or month_num == 4 or month_num == 5:
        if month_num == 3:
            print(f"{month_dict.get('k3')} is {season_dict.get('s1')} month")
        if month_num == 4:
            print(f"{month_dict.get('k4')} is {season_dict.get('s1')} month")
        if month_num == 5:
            print(f"{month_dict.get('k5')} is {season_dict.get('s1')} month")
    if month_num == 6 or month_num == 7 or month_num == 8:
        if month_num == 6:
            print(f"{month_dict.get('k6')} is {season_dict.get('s2')} month")
        if month_num == 7:
            print(f"{month_dict.get('k7')} is {season_dict.get('s2')} month")
        if month_num == 8:
            print(f"{month_dict.get('k8')} is {season_dict.get('s2')} month")
    if month_num == 9 or month_num == 10 or month_num == 11:
        if month_num == 9:
            print(f"{month_dict.get('k9')} is {season_dict.get('s3')} month")
        if month_num == 10:
            print(f"{month_dict.get('k10')} is {season_dict.get('s3')} month")
        if month_num == 11:
            print(f"{month_dict.get('k11')} is {season_dict.get('s3')} month")
