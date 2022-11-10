# Add
def add(num1, num2) -> float:
    return num1 + num2


# Substract
def subtract(num1, num2) -> float:
    return num1 - num2


# Multiply
def multiply(num1, num2) -> float:
    return num1 * num2


# Divide
def divide(num1, num2) -> float:
    return num1 / num2 if (num2 != 0) else 0.0


def show_operations():
    for operation in operations:
        print(operation)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator() -> None:
    should_continue = True
    number1 = float(input("What's the first number? "))
    while should_continue:
        show_operations()
        operation_symbol = input("Pick an operation from the line above: ")
        number2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")
        if input(f"Type 'y' to continuo calculating with {answer}, or type 'n' to exit: ").lower() == "y":
            number1 = answer
        else:
            should_continue = False
            calculator()


calculator()
print("Good Bye")


