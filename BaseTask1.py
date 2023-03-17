# Поработайте с переменными, создайте несколько, выведите на экран, запросите
# у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

name = input("Please call me your name ")
opinion = input(f"Hi! your name is {name} right? (Yes/No)")
lower_opinion = opinion.lower()
answer = "yes"
if lower_opinion == answer:
    second_name = input(f"All right {name}! Now please tell me your second"
                        f" name ")
    sec_opinion = input(f"Thank you {name} now please check your second name\n"
                        f" - {second_name} is she correct? (Yes/No)")
    lower_sec_opinion = sec_opinion.lower()
    if lower_sec_opinion == answer:
        user_age = float(input(f"{name} {second_name} Thank you for your data!"
                               f" Now please tell me, how old are you?"
                               f"(Please input a number!)"))
        int_age = user_age // 1
        third_opinion = input(f"{name} {second_name} you are {int_age} "
                              f"years old? (Yes/No)")
        low_third_opinion = third_opinion.lower()
        if low_third_opinion == answer:
            print(f"{name} {second_name} Thank you! Now i know that you are"
                  f" {int_age} old) See ya!")
        else:
            print(f"{name} {second_name} whats your real age? ")
    else:
        print(f"{name} please tell me correct second name")
else:
    print("Please tell me correct name")
