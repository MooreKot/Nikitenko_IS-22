# В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
# Посчитать количество полученных элементов
import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

poem = re.compile(r'(«[^»]+»)')
matches = poem.findall(text)
unique_matches = list(set(matches))

items_to_remove = ['«Время»', '«Эпоха»', '«делу Петрашевского»']
unique_matches = [i for i in unique_matches if i not in items_to_remove]

print(unique_matches)
print(len(unique_matches))
