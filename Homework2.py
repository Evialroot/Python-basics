"""
2.Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

user_data = int(input("Введите время цифрами в секундах: "))
h = 3600
m = 60
user_hour = user_data // h
user_minute = (user_data - (user_hour * h)) // m
user_sec = (user_data - (user_hour * h + user_minute * m))
print(f"Количество времени: {user_hour:02d}:{user_minute:02d}:{user_sec:02d}")
