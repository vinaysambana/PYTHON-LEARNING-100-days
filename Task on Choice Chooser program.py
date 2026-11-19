'''
Task : Build a Simple Choice Chooser Program:
1 ---> Recrusion logic Factorial
2 ---> Sum of Natural Numbers(recursion)
3 ---> BMI Calculation
4 ---> Fibonacci Series
5 ---> ATM Usecase
any other number ---> only enter 1-5
Q ---> Quit
'''
#========== CHOICE CHOOSER PROGRAM ==========#

print("\n<==========||__CHOICE-CHOOSER-PROGRAM__||==========>\n")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

def bmi_calculation():
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi = weight / (height * height)
    print("Your BMI is:", round(bmi, 2))

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
    
def atm():
    balance = 10000
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Balance:", balance)

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Amount deposited successfully!")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= balance:
                balance -= amount
                print("Please collect your cash.")
            else:
                print("Insufficient balance!")

        elif choice == 4:
            print("Thank you for using ATM!")
            break

        else:
            print("Enter a valid choice!")

while True:
    print("1. Factorial using Recursion")
    print("2. Sum of Natural Numbers using Recursion")
    print("3. BMI Calculation")
    print("4. Fibonacci Series")
    print("5. ATM Usecase")
    print("Q. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        n = int(input("Enter a number: "))

        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial:", factorial(n))

    elif choice == '2':
        n = int(input("Enter a number: "))

        if n < 0:
            print("Enter a positive number!")
        else:
            print("Sum of Natural Numbers:", sum_natural(n))

    elif choice == '3':
        bmi_calculation()

    elif choice == '4':
        n = int(input("Enter number of terms: "))
        fibonacci(n)

    elif choice == '5':
        atm()

    elif choice.upper() == 'Q':
        print("Thank you! Program terminated.")
        break

    else:
        print("Only enter 1-5 or Q!")
