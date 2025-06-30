class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'
    
    def __add__(self, other):
        # Convert other to a string or int depending on context
        if isinstance(self.value, str) and not self.value.isdigit():
            # Treat self as a string, concatenate
            return Silly(str(self.value) + str(other))
        
        if isinstance(other, Silly):
            other_val = other.value
        else:
            other_val = other
        
        # Now we check if both are digit strings or integers
        try:
            result = int(self.value) + int(other_val)
            return Silly(result)
        except ValueError:
            return Silly(str(self.value) + str(other_val))
        

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)