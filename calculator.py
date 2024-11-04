# A Simple Calculator


value1 = float(input('First value: '))
value2 = float(input('Second value: '))

print(
    '''
        Option;

                1. Addition
                2. Subtraction
                3. Division
                #. Exit

    '''
)

option = input('Option: ')
if option == '1':
    result = value1 + value2
    print(f'Result: {result}')

elif option == '2':
    result = value1 - value2
    print(f'Result: {result}')

elif option == '3':
    result = value1 / value2
    print(f'Result: {result}')

else:
    print('Invalid Option')

