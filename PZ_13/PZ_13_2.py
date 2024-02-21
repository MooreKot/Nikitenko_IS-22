# В матрице элементы второго столбца возвести в квадрат.
import random

mtrx = [[random.randint(0, 50) for i in range(2)] for i in range(4)]

def square(mtrx):
    for i in mtrx:
        i[1] = i[1] ** 2
    return mtrx

print(mtrx)
print(square(mtrx))