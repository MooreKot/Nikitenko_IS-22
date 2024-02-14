# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Элементы после сортировки:
# Количество элементов:
# Минимальный элемент кратный 2:
# Максимальный элемент кратный 5:
import random

numbers = []
numbers2 = []
for i in range(7):
    numbers.append(random.randint(0, 100))
    numbers2.append(random.randint(-100, 0))

with open('file1.txt', 'w') as f1:
    f1.write(' '.join(map(str, numbers)))

with open('file2.txt', 'w') as f2:
    f2.write(' '.join(map(str, numbers2)))

with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2, open('output.txt', 'w') as output:
    data1 = list(map(int, f1.read().split()))
    data2 = list(map(int, f2.read().split()))

    data = data1 + data2
    sort_data = sorted(data)
    num = len(sort_data)
    min_2 = min(filter(lambda x: x % 2 == 0, sort_data))
    max_5 = max(filter(lambda x: x % 5 == 0, sort_data))

    output.write(f"Элементы первого и второго файлов:" + str(data) + "\n")
    output.write("Отсортированные элементы: " + str(sort_data) + "\n")
    output.write("Количество элементов: " + str(num) + "\n")
    output.write("Минимальный элемент, кратный 2: " + str(min_2) + "\n")
    output.write("Максимальный элемент, кратный 5: " + str(max_5) + "\n")


