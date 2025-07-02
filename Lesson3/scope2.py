class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f'{self._name} {self.school_name}'
    
    @classmethod
    def get_school(cls):
        return cls.school_name
    

johnny = Student('johnny')
joseph = Student('joseph')

print(Student.school_name)
print(Student.get_school())

print(johnny)
print(joseph)
