#  Даны два целых числа A и B (A < B). Вывести в порядке возрастания все целые числа, расположенные между A и B (включая сами числа A и B), а также количество N этих чисел.
while True:
    try:
        a = int(input('Введите число a: '))
        b = int(input('Введите число b (b > a): '))
        if a >= b:
            print('Введите число b больше a')
            continue
        n = 0
        for i in range(a, b+1):
            print(i)
            n += 1
        print('Количество чисел:', n)
        break
    except ValueError:
        print('Ошибка! Введены некорректные данные.')