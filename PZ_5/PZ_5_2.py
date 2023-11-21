# Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого
# положительного числа K, а также их сумму S (K — входной, C и S — выходные
# параметры целого типа). С помощью этой функции найти количество и сумму цифр
# для каждого из пяти данных целых чисел
import random

def DigitCountSum(K):
    num_str = str(K)  # преобразуем число в строку
    digits = list(map(int, str(num_str)))  # преобразуем каждую цифру в числовой формат и преобразуем объект map в список
    C = len(digits)  # количество цифр равно длине списка digits
    S = sum(digits)  # сумма цифр равна сумме всех элементов списка digits
    print(f'Количество цифр в числе {K}: {C}, сумма цифр: {S}')
    return C, S


K = random.randint(0, 99999)
DigitCountSum(K)
K = random.randint(0, 999)
DigitCountSum(K)
K = random.randint(0, 99999)
DigitCountSum(K)
K = random.randint(0, 9999)
DigitCountSum(K)
K = random.randint(0, 99999)
DigitCountSum(K)
