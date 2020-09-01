#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

allseconds = int(input("Укажите время в секундах = "))

ss = allseconds % 60
allseconds = allseconds // 60
hh = allseconds // 60
mm = allseconds % 60

print(f"Время: {hh:02d}:{mm:02d}:{ss:02d}")