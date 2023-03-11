import time


bday = input('Введите свою дату рождения в формате DD.MM.YYYY:\n')
print(f"Вы прожили {int(time.time()-time.mktime(time.strptime(bday,'%d.%m.%Y'))) // 86400} дней")
