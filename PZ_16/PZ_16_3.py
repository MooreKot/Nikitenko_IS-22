# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle

class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

def save_def(info_cars, fname):
    with open(fname, 'wb') as f:
        pickle.dump(info_cars, f)

def load_def(fname):
    with open(fname, 'rb') as f:
        info_cars = pickle.load(f)
    return info_cars

    def info(self):
        print(f'"Марка: {self.mark}, Модель: {self.model}, Год выпуска: {self.year}')


car1 = Car('Toyota', 'Corolla', 2015)
car2 = Car('Honda', 'Civic', 2018)
car3 = Car('Ford', 'Focus', 2012)

info_cars = [car1, car2, car3]
save_def(info_cars, 'cars.pkl')

loaded = load_def('cars.pkl')
for i in loaded:
    print(f"Mark: {i.mark}, Model: {i.model}, Year: {i.year}")


