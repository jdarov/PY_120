list_of_numbers = list(input("Please enter a list of numbers: "))


try:
    list_of_numbers = [1/int(number) for number in list_of_numbers if not number.isspace()]
except (ValueError, ZeroDivisionError):
    print("You didn't enter a number or can't divide by 0")