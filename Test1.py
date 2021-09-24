from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    @staticmethod
    def get_payment_rate():
        return 100


class Personal(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    @abstractmethod
    def get_rate(self):
        pass


class Teacher(Personal):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def get_rate(self):
        return 500


class Director(Personal):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def get_rate(self):
        return 1000


class ViceDirector(Personal):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def get_rate(self):
        return 700


class Cleaner(Personal):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def get_rate(self):
        return 200


school_personal = [
    Teacher('a', 'b'),
    Director('c', 'd'),
    Cleaner("f", "e"),
    ViceDirector("f", "d")
]
students = [
    Student("vova", "pupkin"),
    Student("vasya", "pupkin"),
    Student("olga", "pupkina")
]
budget = sum(p.get_rate() for p in school_personal)
print("Budget =", budget)
students_capacity = sum(p.get_payment_rate() for p in students)
if students_capacity >= budget:
    print("enough student to cover personal budget")
else:
    deficit = budget - students_capacity
    print(f"Budget deficit = {deficit}")
    students_are_needed = deficit // (students_capacity / len(students))
    print("Students_are_needed =", str(students_are_needed))
