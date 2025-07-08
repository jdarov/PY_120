class Greeting:

    @staticmethod
    def greet(message='Hi'):
        print(message)

class Hello(Greeting):

    @classmethod
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

hello = Hello()

Greeting.greet() #Hello
hello.greet("goodbye") #goodbye

Hello.hi() 