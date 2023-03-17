# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.

num1 = input("Have a good day! Please input a positive number do you like")
num2 = num1 + num1
num3 = num1 + num1 + num1
num_int = int(num1)
if num_int > 0:
    num_int2 = int(num2)
    num_int3 = int(num3)
    sum = num_int + num_int2 + num_int3
    print(f"Thank you!\n The sum of {num_int} + {num_int2} + {num_int3} is"
          f" {sum}")
else:
    print("Please input a correct number")