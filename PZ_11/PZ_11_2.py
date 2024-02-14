# Из предложенного текстового файла (text18-25.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно удалив букву «с» из
# текста.

with open('text18-25.txt', 'r', encoding='utf-16') as f1:
    content = f1.read()
    print(content)

letter = 0
for i in content:
    if i.isalpha():
        letter += 1
print(f'Количество букв в файле: {letter}')

content_without_s = content.replace('с', '')
with open('text18.txt', 'w') as f2:
    f2.write(content_without_s)
