# Calculator With Function

print(" * Welcome to Dreezzy's Calculator * ")
print("To make it your calculator.")
user = input('Enter your Nickname: ')
print(f"\n * Welcome to {user}'s Calculator")


value1 = float(input('Enter First Value: '))
value2 = float(input('Enter Second Value: '))

def dashboard():
    print(
        '''
        * This is a Simple Calculator Built with Python Function * 

        Option:
            1. Addition
            2. Subtraction
            3. Division
            4. Modulus
            5. Multiplication
            6. Exponentiation
            #. Exit

        '''
    )
    option = input('Option: ')
    if option == "1":
        plus()
    elif option == '2':
        minus()
    elif option == "3":
        divide()
    elif option == '4':
        remainder()
    elif option == '5':
        multiply()
    elif option == '6':
        exponential()
    else:
        print('Goodbye....')
        exit()

def plus():
    print("Performing the calculation...")
    Ans = value1 + value2
    print(f"Answer: {Ans}")
    repeat()

def minus():
    Ans = value1 - value2
    print(f"Answer: {Ans}")
    repeat()

def divide():
    Ans = value1 / value2
    print(f"Answer: {Ans}")
    repeat()

def remainder():
    Ans = value1 % value2
    print(f"Answer: {Ans}")
    repeat()

def multiply():
    Ans = value1 * value2
    print(f"Answer: {Ans}")
    repeat()

def exponential():
    Ans = value1 ** value2
    print(f"Answer: {Ans}")
    repeat()

def repeat():
    repeat = input("Do you want to perform another calculation with same value? (yes/no): ").strip().lower()
    if repeat == 'yes':
        return dashboard()
    else:
        print('Goodbye....')
        exit()

dashboard()

