#My Python Calculator (Kinda)

def Primary_operation():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for exponent
    ''')

Primary_operation()


number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
    input('Press "Enter" for new operation :) ')
    Primary_operation()

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
    input('Press "Enter" for new operation :) ')
    Primary_operation()

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
    input('Press "Enter" for new operation :) ')
    Primary_operation()

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
    input('Press "Enter" for new operation :) ')
    Primary_operation()

elif operation == '**':
    print(number_1 ** number_2)
    input('Press "Enter" for new operation :) ')
    Primary_operation()

else:
    print('You have not typed a valid operator, please run the program again.')