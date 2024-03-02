# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти среднее значение продаж по
# каждому виду продукции, результаты вывести на экран.

fruits = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
sales = dict()
key = None
for i in fruits.split():
    if i.isdigit():
        sales[key].append(int(i))
    else:
        key = i
        sales[key] = []

sred = sum(sales['апельсины']) / len(sales['апельсины'])
sredn = sum(sales['яблоки']) / len(sales['яблоки'])
print(f'Продукция: {sales}')
print(f'Среднее значение продаж апельсинов: {sred}')
print(f'Среднее значение продаж яблок: {sredn}')