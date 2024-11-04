# Mini Calculator with class

print(" * Welcome to Dreezzy's Calculator * ")
print("To make it your calculator.")
user = input('Enter your Nickname: ')
print(f"\n * Welcome to {user}'s Calculator")


value1 = float(input('Enter First Value: '))
value2 = float(input('Enter Second Value: '))



class Calculator:
    def __init__(self):
        self.name = 'My Calculator'
    

    def dashboard(self):
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
            self.plus()
        elif option == '2':
            self.minus()
        elif option == "3":
            self.divide()
        elif option == '4':
            self.remainder()
        elif option == '5':
            self.multiply()
        elif option == '6':
            self.exponential()
        else:
            print('Goodbye....')
            exit()

    def plus(self):
        print("Performing the calculation...")
        self.Ans = value1 + value2
        print(f"Answer: {self.Ans}")
        self.repeat()

    def minus(self):
        self.Ans = value1 - value2
        print(f"Answer: {self.Ans}")
        self.repeat()

    def divide(self):
        self.Ans = value1 / value2
        print(f"Answer: {self.Ans}")
        self.repeat()

    def remainder(self):
        self.Ans = value1 % value2
        print(f"Answer: {self.Ans}")
        self.repeat()

    def multiply(self):
        self.Ans = value1 * value2
        print(f"Answer: {self.Ans}")
        self.repeat()

    def exponential(self):
        self.Ans = value1 ** value2
        print(f"Answer: {self.Ans}")
        self.repeat()

    def repeat(self):
        repeat = input("Do you want to perform another calculation with same value? (yes/no): ").strip().lower()
        if repeat == 'yes':
            return self.dashboard()
        else:
            print('Goodbye....')
            exit()

calculate = Calculator()
calculate.dashboard()


