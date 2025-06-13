def calculator():
    """A simple yet enhanced calculator program."""

    print("Welcome to the Enhanced Calculator!")
    print()

    def get_number_input(prompt):
        """Gets a valid integer or float input from the user."""
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_operator_input():
        """Gets a valid operator input from the user."""
        while True:
            operator = input("Enter the operator [+,-,*,/,//,%,**]: ").strip()
            if operator in ['+', '-', '*', '/', '//', '%', '**']:
                return operator
            else:
                print("Invalid operator. Please choose from +, -, *, /, //, %, **")

    def calculate(num1, num2, operator):
        """Performs the calculation based on the operator."""
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error! Division by zero."
            return num1 / num2
        elif operator == '//':
            if num2 == 0:
                return "Error! Integer division by zero."
            return num1 // num2
        elif operator == '%':
            if num2 == 0:
                return "Error! Modulo by zero."
            return num1 % num2
        elif operator == '**':
            return num1 ** num2
        return "Error: Invalid operator (this should not happen)."

    def perform_operation(num1=None, num2=None):
        """Takes input, performs calculation, and asks for further operations."""
        if num1 is None or num2 is None:
            print("\nEnter numbers for the calculation:")
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")
            print()

        operator = get_operator_input()
        result = calculate(num1, num2, operator)
        print(f"Result: {num1} {operator} {num2} = {result}")
        print()

        while True:
            choice = input("Choose next action:\n1. Use the result as the first number for a new operation\n2. Use the same numbers for another operation\n3. Enter new numbers\n4. Exit\nEnter your choice (1-4): ").strip()
            if choice == '1':
                perform_operation(num1=result)
                break
            elif choice == '2':
                perform_operation(num1=num1, num2=num2)
                break
            elif choice == '3':
                perform_operation()
                break
            elif choice == '4':
                print("Thank you for using the Enhanced Calculator!")
                return
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    perform_operation()

if __name__ == "__main__":
    calculator()