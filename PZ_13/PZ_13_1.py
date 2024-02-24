# В матрице найти сумму элементов второй половины матрицы.
import random

mtrx = [[random.randint(0, 50) for i in range(4)] for i in range(4)]
def summa(mtrx):
    mtrx_sum = sum([mtrx[i][j] for i in range(4) for j in range(4) if j >= 2])
    return mtrx_sum

print(mtrx)
print(summa(mtrx))