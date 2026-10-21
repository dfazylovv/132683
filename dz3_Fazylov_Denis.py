number = input("Введите число от 0 до 99: ")

if not number.isdigit():
    print("Вы должны ввести целое число")
else:
    number = int(number)

    if number > 99:
        print("Число должно быть в диапазоне от 0 до 99")

    elif number == 0:
        print("ноль")

    elif number < 10:
        if number == 1:
            print("один")
        elif number == 2:
            print("два")
        elif number == 3:
            print("три")
        elif number == 4:
            print("четыре")
        elif number == 5:
            print("пять")
        elif number == 6:
            print("шесть")
        elif number == 7:
            print("семь")
        elif number == 8:
            print("восемь")
        elif number == 9:
            print("девять")

    elif number < 20:
        if number == 10:
            print("десять")
        elif number == 11:
            print("одиннадцать")
        elif number == 12:
            print("двенадцать")
        elif number == 13:
            print("тринадцать")
        elif number == 14:
            print("четырнадцать")
        elif number == 15:
            print("пятнадцать")
        elif number == 16:
            print("шестнадцать")
        elif number == 17:
            print("семнадцать")
        elif number == 18:
            print("восемнадцать")
        elif number == 19:
            print("девятнадцать")

    else:
        if number // 10 == 2:
            print("двадцать", end=" ")
        elif number // 10 == 3:
            print("тридцать", end=" ")
        elif number // 10 == 4:
            print("сорок", end=" ")
        elif number // 10 == 5:
            print("пятьдесят", end=" ")
        elif number // 10 == 6:
            print("шестьдесят", end=" ")
        elif number // 10 == 7:
            print("семьдесят", end=" ")
        elif number // 10 == 8:
            print("восемьдесят", end=" ")
        elif number // 10 == 9:
            print("девяносто", end=" ")

       
        if number % 10 == 1:
            print("один")
        elif number % 10 == 2:
            print("два")
        elif number % 10 == 3:
            print("три")
        elif number % 10 == 4:
            print("четыре")
        elif number % 10 == 5:
            print("пять")
        elif number % 10 == 6:
            print("шесть")
        elif number % 10 == 7:
            print("семь")
        elif number % 10 == 8:
            print("восемь")
        elif number % 10 == 9:
            print("девять")