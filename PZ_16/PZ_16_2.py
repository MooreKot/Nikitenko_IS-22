# Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров.

class Avtomobil:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

class Gruzovik(Avtomobil):
    def __init__(self, mark, model, year, gruz_pod):
        Avtomobil.__init__(self, mark, model, year)
        self.gruz_pod = gruz_pod

class Legkovoi(Avtomobil):
    def __init__(self, mark, model, year, col_pas):
        Avtomobil.__init__(self, mark, model, year)
        self.col_pas = col_pas

avto1 = Avtomobil('Lada', 'Granta', 2013)
avto2 = Gruzovik('ЗИЛ', 130, 2010, 7500)
avto3 = Legkovoi('BMW', 'X5', 2017, 5)

print(avto1.__dict__)
print(avto2.__dict__)
print(avto3.__dict__)