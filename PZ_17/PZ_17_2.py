# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9.

import tkinter as tk

window = tk.Tk()
window.title("Проверка координат точки")
window.geometry('520x160')


def check_coordinates():
    x = int(x_entry.get())
    y = int(y_entry.get())
    result = (x < 0) and (y > 0)
    result_label.config(text=f"Точка с координатами ({x}, {y}) лежит во второй координатной четверти: {result}")


x_label = tk.Label(window, text="Введите x:")
x_entry = tk.Entry(window)

y_label = tk.Label(window, text="Введите y:")
y_entry = tk.Entry(window)


check_button = tk.Button(window, text="Проверить", command=check_coordinates)


result_label = tk.Label(window)

x_label.pack()
x_entry.pack()

y_label.pack()
y_entry.pack()

check_button.pack()

result_label.pack()

window.mainloop()
