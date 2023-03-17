#Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма
#(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение. Если фирма отработала с прибылью,
#вычислите рентабельность выручки (соотношение прибыли к выручке).
#Далее запросите численность сотрудников фирмы и определите
#прибыль фирмы в расчете на одного сотрудника.

income = int(input("Have a good day! Please input a number of income do you"
                   " have "))
outgoings = int(input("Now please input a number of outgoings do you have "))
if income > outgoings:
    profit = income - outgoings
    profitability = (profit / income) * 100
    round_profitability = round(profitability, 2)
    print(f" Your company's income is bigger than your outgoings!"
          f" Congratulation! Your company made a profit!")
    if round_profitability > 21:
        print(f"Congratulation! Your company have {round_profitability}% of "
              f"profitability - it is high profitability - super profitable "
              f"business")
    elif round_profitability > 5 and round_profitability <= 20:
        print(f"Congratulation! Your company have {round_profitability}% "
              f"of profitability - it is medium profitability - your company "
              f"is stable")
    else:
        print(f"Your company have {round_profitability}% of profitability "
              f"it is a low profitability - your company need optimization!")
    staff = float(input("Now please input a number of staff that do you have "))
    staff_int = staff // 1
    one_person_income = profit / staff_int
    round_one_per_inc = round(one_person_income, 2)
    print(f"Your company have {round_one_per_inc} earnings by one person")
else:
    print("Your company's outgoings is bigger than your income!!"
          " Your company is work at a loss, try harder!")