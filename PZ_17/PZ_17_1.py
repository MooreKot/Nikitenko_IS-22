# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).

import tkinter as tk

# Заголовок
window = tk.Tk()
window.title("Форма заявки")
window.geometry('450x450')

header = tk.Label(window, text="Форма заявки", bg="green", fg="white", font=("Arial", 15))
header.grid(row=0, column=0, columnspan=4, sticky="ew")
text = tk.Label(window, text=f"Допустимые типы вложений: zip, rar, txt, doc, jpg, png, gif, odt, xml")
text.grid(row=1, column=0, sticky="w", columnspan=4)

text_2 = tk.Label(window, text=f"Макс. размер каждого файла: 1024kb.")
text_2.grid(row=2, column=0, sticky="w", columnspan=4)
text_3 = tk.Label(window, text=f"Макс. общий размер файла: 2048kb.")
text_3.grid(row=3, column=0, sticky="w", columnspan=4)

# Форма для заполнения
name_label = tk.Label(window, text="Ваше имя:")
name_label.grid(row=4, column=0, sticky="e")
name_entry = tk.Entry(window)
name_entry.grid(row=4, column=1, sticky="w")

email_label = tk.Label(window, text="Ваш email:")
email_label.grid(row=5, column=0, sticky="e")
email_entry = tk.Entry(window)
email_entry.grid(row=5, column=1, sticky="w")

subject_label = tk.Label(window, text="Тема письма:")
subject_label.grid(row=6, column=0, sticky="e")
subject_entry = tk.Entry(window)
subject_entry.grid(row=6, column=1, sticky="w")

attachment_label = tk.Label(window, text="Прикрепить файл:")
attachment_label.grid(row=7, column=0, sticky="e")
attachment_entry = tk.Entry(window)
attachment_entry.grid(row=7, column=1, sticky="w")
attachment_button = tk.Button(window, text="Обзор...")
attachment_button.grid(row=7, column=2, sticky="w")


attachment_label_2 = tk.Label(window, text="Прикрепить файл:")
attachment_label_2.grid(row=8, column=0, sticky="e")
attachment_entry_2 = tk.Entry(window)
attachment_entry_2.grid(row=8, column=1, sticky="w")
attachment_button_2 = tk.Button(window, text="Обзор...")
attachment_button_2.grid(row=8, column=2, sticky="w")

attachment_label_3 = tk.Label(window, text="Прикрепить файл:")
attachment_label_3.grid(row=9, column=0, sticky="e")
attachment_entry_3 = tk.Entry(window)
attachment_entry_3.grid(row=9, column=1, sticky="w")
attachment_button_3 = tk.Button(window, text="Обзор...")
attachment_button_3.grid(row=9, column=2, sticky="w")

message_label = tk.Label(window, text="Ваше сообщение:")
message_label.grid(row=10, column=0, sticky="e")
message_text = tk.Text(window, height=7, width=40)
message_text.grid(row=11, column=1, sticky="w", columnspan=3)

button_frame = tk.Frame(window, bg="green")
button_frame.grid(row=12, column=0, columnspan=4, sticky="ew")

# Кнопки
send_button = tk.Button(button_frame, text="Отправить email")
send_button.pack(side="left", padx=80)
clear_button = tk.Button(button_frame, text="Отчистить")
clear_button.pack(side="left")
window.mainloop()
