from art import logo


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


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    while True:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        num2 = float(input("What's the next number? "))
        operation = operators[operator]
        answer = operation(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        play_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if play_again == 'y':
            num1 = answer
        elif play_again == 'n':
            calculator()
            break

calculator()
    

