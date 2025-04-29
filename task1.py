import random


# Генерація секретного коду з 4 різних цифр
code = random.sample("0123456789", 4)
print("Загадано 4-значний код. Вгадай його! (Цифри різні)")


while True:
   guess = input("Введи свою спробу: ")


   # Перевірка введення (4 цифри, всі різні)
   if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
       print("Помилка! Введи 4 різні цифри.")
       continue


   # Підрахунок биків (цифри на правильних місцях)
   bulls = sum(guess[i] == code[i] for i in range(4))


   # Підрахунок корів (цифри на неправильних місцях)
   cows = sum(c in code for c in guess) - bulls


   print(f"Бики: {bulls}, Корови: {cows}")


   # Перевірка на виграш
   if bulls == 4:
       print("Ти вгадав код! Вітаю!")
       break
