class Foo:

    def __init__(self):
        type_name = type(self).__name__
        print(f'I am a {type_name} object')

foo = Foo()
print(f'I am a {foo.__class__.__name__} object')