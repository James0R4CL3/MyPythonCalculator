#My Python Calculator (Kinda)

def main():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for exponent
    ''')


    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        input('Press "Enter" for new operation :) ')
        main()


    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        input('Press "Enter" for new operation :) ')
        input('Press "Enter" for new operation :) ')
        main()

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        input('Press "Enter" for new operation :) ')
        input('Press "Enter" for new operation :) ')
        main()

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
        input('Press "Enter" for new operation :) ')
        input('Press "Enter" for new operation :) ')
        main()

    elif operation == '**':
        print(number_1 ** number_2)
        input('Press "Enter" for new operation :) ')
        input('Press "Enter" for new operation :) ')
        main()

    else:
        print('You have not typed a valid operator, please run the program again.')
        input('Press "Enter" for new operation :) ')
        main()
main()