class NegativeNumberError(Exception):
    pass

number = int(input('Type a number: '))
if number < 0:
    raise NegativeNumberError("The number must be greater than 0")
print(f'The number is {number}')

