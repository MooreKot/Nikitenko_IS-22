#  Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE, если не является — вывести FALSE.
while True:
    try:
        n = int(input('Введите число: '))
        if n < 0:
            print('Ошибка! Введите положительное число')
            continue
        while n % 3 == 0:
            n /= 3
        if n == 1:
            print("TRUE")
        else:
            print("FALSE")
        break
    except ValueError:
        print('Ошибка! Введите целое число.')