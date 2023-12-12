# Даны два списка A и B одинакового размера N. Сформировать новый список C того
# же размера, каждый элемент которого равен максимальному из элементов списков
# A и B.
while True:
    try:
        C = []

        string = input('Введите числа через пробел: ')
        nums = string.split()
        A = []
        for i in nums:
            if i.isdigit():
                A.append(int(i))
            else:
                raise ValueError

        string = input('Введите числа через пробел: ')
        nums = string.split()
        B = []
        for i in nums:
            if i.isdigit():
                B.append(int(i))
            else:
                raise ValueError

        for i in range(len(A)):
            C.append((max([A[i], B[i]])))
        print(C)
        break
    except ValueError:
        print('Ошибка! Введите числа.')