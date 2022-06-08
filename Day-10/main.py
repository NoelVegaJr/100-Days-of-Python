from art import logo

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    try:
        return n1 / n2
    except:
        return 0


while True: 
    print(logo)
    num1 = int(input("What's the first number?: "))

    while True:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        num2 = int(input("What's the next number? "))

        if operator == '+':  
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
            
        print(f"{num1} {operator} {num2} = {result}")

        play_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if play_again == 'y':
            num1 = result
        elif play_again == 'n':
            break

    
    

