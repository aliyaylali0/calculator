import art
def add(n1,n2):
    return n1 + n2

def extraction(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operation = {
    "+": add,
    "-": extraction,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)
    n1 = float(input("What's the first number: "))



    for a in operation:
        print(a)
    calculator_running = True

    while calculator_running:


        cal = input("Pick an operation: ")
        n2 = float(input("What's the next number: "))
        calculation_funcsion = operation[cal]
        answer = calculation_funcsion(n1,n2)

        print(f"{int(n1)}{cal}{int(n2)} = {answer}")


        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
            n1 = answer
        else:

            calculator_running = False
            calculator()


calculator()



