#Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

num_of_sec = float(input("Have a good day! Please input how much seconds do"
                         " you like "))
sec = num_of_sec // 1
minute = sec // 60
hour = minute // 60
print(f"We have | {hour} hours | {minute} minutes | {sec} seconds ")