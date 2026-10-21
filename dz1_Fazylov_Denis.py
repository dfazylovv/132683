import random as rd

a = rd.randint(0, 10)
b = int(input("Угадай число: "))

while b != a:
    if b < a:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    b = int(input("Попробуй ещё: "))
print("Угадал!")
