def get_operation(choice):
    choice = choice.strip().lower()
    exit_terms = ["5", "e", "exit", "quit", "q", "bye"]

    if choice in exit_terms:
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
        else:
            print("This operation is not yet implemented.")

if __name__ == "__main__":
    main()