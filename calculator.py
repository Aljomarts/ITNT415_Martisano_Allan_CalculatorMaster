def get_number(prompt):
    """Prompt the user until a valid float is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def get_operation(choice):
    choice = choice.strip().lower()
    addition_terms = ["1", "a", "add", "addition", "plus", "sum"]
    subtraction_terms = ["2", "b", "sub", "subtract", "subtraction", "minus"]
    exit_terms = ["5", "e", "exit", "quit", "q", "bye"]
    if choice in addition_terms:
        return "add"
    elif choice in subtraction_terms:
        return "subtract"
    elif choice in exit_terms:
        return "exit"
    else:
        return None

def main():
    while True:
        print("\n=== Calculator Menu ===")
        print("1 / A / Add       - Addition")
        print("2 / B / Sub       - Subtraction")
        print("3 / C / Mul       - Multiplication")
        print("4 / D / Div       - Division")
        print("5 / E / Exit      - Exit")
        choice = input("Enter your choice: ")
        operation = get_operation(choice)
        if operation == "exit":
            print("Goodbye!")
            break
                elif operation == "add":
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"Result: {add(num1, num2)}")
        elif operation == "subtract":
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"Result: {subtract(num1, num2)}"))
        else:
            print("This operation is not yet implemented.")

if __name__ == "__main__":
    main()