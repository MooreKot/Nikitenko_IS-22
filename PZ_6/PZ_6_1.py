# Дан целочисленный список размера N. Проверить, чередуются ли в нем четные и
# нечетные числа. Если чередуются, то вывести 0, если нет, то вывести порядковый
# номер первого элемента, нарушающего закономерность.

def Alternation(nums):
    for i in range(1, len(nums)):
        if nums[i] % 2 == nums[i-1] % 2:
            return i
    return 0

while True:
    try:
        string = input('Введите несколько чисел через пробел: ')
        string = string.split()
        nums = []
        for i in string:
            if i.isdigit():
                nums.append(int(i))
            else:
                raise ValueError

        result = Alternation(nums)
        print(result)
        break
    except ValueError:
        print('Ошибка! Введите числа.')