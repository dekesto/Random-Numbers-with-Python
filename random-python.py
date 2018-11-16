import random


def random_number():
    print("Enter Minimum, Maximum and Amount of numbers to be generated...")
    min = int(input("Min: "))
    max = int(input("Max: "))
    amount = int(input("Amount of numbers: "))
    numbers = [random.randint(min, max) for i in range(amount)]
    print(','.join(str(n) for n in numbers))


random_number()
