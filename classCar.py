
class Car:
    count = 0

    def __init__(self, color):
        Car.count += 1
        self.color = color
        self.wheels = 4
        self.spare = 0

    @classmethod
    def get_count(cls):
        print('Amount of cars: {}'.format(cls.count))

    def get_col_spare(self):
        if self.color == 'black':
            return self.spare + 1
        else:
            return self.spare

    def get_diag(self):
        print('Color, Wheels, Spares: {}, {}, {}'.
              format(self.color, self.wheels, self.get_col_spare()))


r = Car('black')
r.get_diag()


r1 = Car('red')
r1.get_diag()

r2 = Car('yellow')
r2.get_diag()

r3 = Car('blue')
r3.get_diag()

Car.get_count()

