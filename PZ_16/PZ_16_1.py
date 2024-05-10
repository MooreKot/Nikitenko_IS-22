# Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска".
# Напишите метод, который выводит информацию о машине в формате "Марка:
# марка, Модель: модель, Год выпуска: год".

class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def info(self):
        print(f'"Марка: {self.mark}, Модель: {self.model}, Год выпуска: {self.year}')

car1 = Car('Lada', 'Granta', 2012)
car1.info()