# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить функцией с параметрами. Значения n и m программа должна запрашивать.
while True:
    try:
        n = int(input('Введите первое число: '))
        m = int(input('Введите второе число: '))
        def summa(n, m):
            summ = 0
            for i in range(n, m+1):
                summ += i
            print(f'Сумма чисел от {n} до {m} равна {summ}.')
        summa(n, m)
        break
    except ValueError:
        print('Ошибка! Введите целое число.')