digits = '0123456789ABCDEF'

def decimal_to_binary(number, system=2):
    final = ''
    while number > 0:
        final = digits[number % system] + final
        number //= system
    return final

def binary_to_decimal(number, system=2):
    final = 0
    for digit in number:
        final = final * system + digits.index(digit)
    return final

def sixteen_to_decimal(number, system=16):
    final = 0
    for digit in number:
        final = final * system + digits.index(digit)
    return final

def decimal_to_any(number, system):
    final = ''
    while number > 0:
        final = digits[number % system] + final
        number //= system
    return final

def any_to_decimal(number, system):
    final = 0
    for digit in number:
        final = final * system + digits.index(digit)
    return final

def main():
    number = input("Enter a number (if decimal - without prefix, if binary - with prefix 0b) : ")
    while not (number[0:2] == "0b" or number.isdecimal() or number[0:2] == "0x" or number[-2] == 'x' or number[-3] == 'x'):
        number = input("Enter a number (if decimal - without prefix, if binary - with prefix 0b) : ")

    if number[0:2] == '0b':
        print(f"Your number {number} in decimal - {binary_to_decimal(number[2:])}")

    elif number[0:2] == '0x':
        decimal_from_16 = sixteen_to_decimal(number[2:])
        what_system = input("What system do you want to convert to? (decimal - d, binary - b) : ")
        if what_system == 'd':
            print(f"Your number {number} in hexadecimal number system - {decimal_from_16}")
        else:
            print(f"Your number {number} in hexadecimal number system - {decimal_to_binary(decimal_from_16)}")

    elif number[-2] == 'x':
        to_decimal = any_to_decimal(number[:-2], int(number[-1]))
        what_system = int(input(f"To what system do u want to convert number {number[-2]}? : "))
        print(decimal_to_any(to_decimal, what_system))

    elif number[-3] == 'x':
        to_decimal = any_to_decimal(number[:-3], int(number[-2:]))
        what_system = int(input(f"To what system do u want to convert number {number[-2]}? : "))
        print(decimal_to_any(to_decimal, what_system))

    else:
        print(f"Your number {number} in binary - {decimal_to_binary(int(number))}")

    again = input("Do you want to repeat? y/n : ")
    if again == 'y':
        main()
    else:
        print("Ok! Seeyuh")

main()