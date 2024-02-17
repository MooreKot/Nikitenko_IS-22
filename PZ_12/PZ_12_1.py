# Дана последовательность целых чисел.
# Поменять местами ее первую и последнюю трети
import random
num = [random.randint(0,100) for i in range(9)]
def swap(num):
    third = len(num) // 3
    return num[-third:] + num[third:-third] + num[:third]

print(num)
print(swap(num))