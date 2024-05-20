
while True:

    number1 = int(input("Enter a number: "))
    operation = int(input("1. +\n2. -\n3. *\n4. /\nEnter a operation:"))
    number2 = int(input("Enter a number: "))

    match operation:
        case 1:
            print(number1 + number2)
        case 2:
            print(number1 - number2)
        case 3:
            print(number1 * number2)
        case 4:
            if number2 == 0:
                print("Division by zero!")
            else:
                print(number1 / number2)

    if input("Do you want to continue?\nEnter Y or N:") in "N":
        break


