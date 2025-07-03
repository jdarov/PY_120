first_number = input('Please enter a number: ')
second_number = input('Please enter a 2nd number: ')

try:
    divide = int(first_number) / int(second_number)
except (ValueError, ZeroDivisionError) as ze:
    print(ze, "You need to enter a numbe greater than zero", sep='\n')
else:
    print(divide)
finally:
    print("End of program!")
