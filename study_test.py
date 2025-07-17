# class Employee:
#     EMPLOYEE_COUNT = 0
#     ROLE_DISTRIBUTION = {}

#     def __init__(self, name, role):
#         self._name = name
#         self._role = role
#         Employee.EMPLOYEE_COUNT += 1
#         Employee.ROLE_DISTRIBUTION[self._role] = Employee.ROLE_DISTRIBUTION.get(self._role, 0) + 1

#     @classmethod
#     def get_employee_count(cls):
#         return cls.EMPLOYEE_COUNT
#     @classmethod
#     def get_role_distribution(cls):
#         return cls.ROLE_DISTRIBUTION

# emp1 = Employee('Srdjan', 'Engineer')
# emp2 = Employee('Chris', 'Manager')
# emp3 = Employee('Pete', 'Engineer')

# print(Employee.get_employee_count())       # 3
# print(Employee.get_role_distribution())
# # {'Engineer': 2, 'Manager': 1}

# class Engine:
#     def start(self):
#         return f'The engine has started!'

# class Car:

#     def __init__(self, make, model):
#         self._make = make
#         self._model = model

#         self._engine = Engine()

#     def drive(self):
#         print(self._engine.start())
#         print("Car is driving...")

# truck = Car("ford", "f150")

# truck.drive()


class Dog:
    NUMBER_OF_DOGS = 0

    def __init__(self, name):
        self.name = name
        Dog.NUMBER_OF_DOGS += 1

    @classmethod
    def info(cls):
        print('All dogs are good dogs!')
    
    @classmethod
    def number_of_dogs(cls):
        return cls.NUMBER_OF_DOGS

benji = Dog('Benji')
print(Dog.NUMBER_OF_DOGS)
fido = Dog('Fido')
benji.info()        # All dogs are good dogs!
Dog.info()          # All dogs are good dogs!

print(Dog.NUMBER_OF_DOGS)
print(Dog.number_of_dogs())

print(benji.number_of_dogs())
print(benji.NUMBER_OF_DOGS)