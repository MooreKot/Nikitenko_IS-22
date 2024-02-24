# В матрице элементы второго столбца возвести в квадрат.
import random

mtrx = [[random.randint(0, 50) for i in range(2)] for i in range(4)]

def square(mtrx):
    mtrx_square = [mtrx[i][j] ** 2 for i in range(4) for j in range(2) if j == 1]
    return mtrx_square

print(mtrx)
print(square(mtrx))