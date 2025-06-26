# Python 120: Object-Oriented Programming (OOP) Overview

Welcome to the **Python 120 - Object-Oriented Programming (OOP)** section of my studies!  
This README is a summary and reference of key OOP concepts in Python, covering everything from class creation to inheritance and polymorphism.

---

## 🧠 Core Concepts of OOP

### 📦 1. **Classes and Objects**
- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Fido")
print(my_dog.bark())  # Fido says woof!
```

---

### 🧬 2. **Instantiation**
- Instantiation is the process of creating an object from a class.
- The `__init__()` method is the constructor.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

cat = Animal("Whiskers", "Cat")  # ← Instantiation
```

---

### 🛡 3. **Encapsulation**
- Restricting direct access to some components of an object.
- Achieved using naming conventions:
  - `_protected`: internal use, not enforced
  - `__private`: name mangled to prevent external access

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)  # AttributeError!
```

---

### 👨‍👧 4. **Inheritance**
- Enables one class to inherit attributes and methods from another.
- Promotes code reuse and hierarchical relationships.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

buddy = Dog("Buddy")
print(buddy.speak())  # Buddy says woof!
```

---

### 🔁 5. **Polymorphism**
- Objects of different classes can be treated as if they are of the same class, using the same interface (method names).
- Promotes flexibility and interchangeable components.

```python
class Bird:
    def speak(self):
        return "Tweet!"

class Cow:
    def speak(self):
        return "Moo!"

def animal_says(animal):
    print(animal.speak())

animal_says(Bird())  # Tweet!
animal_says(Cow())   # Moo!
```

---

## 🧰 Key OOP Features Recap

| Concept         | Description                                                                 |
|----------------|------------------------------------------------------------------------------|
| **Class**       | Blueprint for creating objects                                              |
| **Object**      | An instance of a class                                                      |
| **Instantiation** | The act of creating an object                                             |
| **Encapsulation** | Hiding internal object details to protect state                           |
| **Inheritance** | Creating a class from another to reuse and extend behavior                  |
| **Polymorphism** | Ability to use a unified interface for different underlying forms (types)  |

---

## 📚 Resources

- [Real Python - OOP Concepts](https://realpython.com/python3-object-oriented-programming/)
- [Python Docs - Classes](https://docs.python.org/3/tutorial/classes.html)
- [freeCodeCamp OOP in Python](https://www.freecodecamp.org/news/object-oriented-programming-in-python/)

---

Happy coding! 🐍
