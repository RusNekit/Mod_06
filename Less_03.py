# class Human:
#     def __init__(self, name, grop):
#         self.name = name
#         super().__init__(grop)
#         super().about()
#
#     def info(self):
#         print(f'My name is {self.name}')
#
#
# class StudentGrop:
#     def __init__(self, grop):
#         self.grop = grop
#
#     def about(self):
#         print(f'{self.name} study in group {self.grop}')
#
#
# class Student(Human, StudentGrop):
#     def __init__(self, name, place, grop):
#         super().__init__(name, grop)
#         self.place = place
#         super().info()
#
#
# print(Student.mro())
# student = Student('Kirill', 'Urban', '111')

import random


class Animal:
    _DEGREE_OF_DANGER = 0
    sound = None
    live = True

    def __init__(self, speed):
        self._cords = [0,0,0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print('Be careful, im attacking you 0_0')

    def speak(self):
        print(self.sound)


class Bird:
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1,4)} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self.speed //= 2
        self._cords[2] -= dz * self.speed


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"



db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()