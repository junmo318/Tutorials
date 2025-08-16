class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        return a ** b


def main():
    calc = Calculator()
    
    print("Simple Calculator")
    print("Available operations: +, -, *, /, ** (power), q (quit)")
    
    while True:
        try:
            print("\nEnter operation:")
            operation = input("Operation (+, -, *, /, **, q): ").strip()
            
            if operation.lower() == 'q':
                print("Goodbye!")
                break
            
            if operation not in ['+', '-', '*', '/', '**']:
                print("Invalid operation. Please use +, -, *, /, or **")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if operation == '+':
                result = calc.add(num1, num2)
            elif operation == '-':
                result = calc.subtract(num1, num2)
            elif operation == '*':
                result = calc.multiply(num1, num2)
            elif operation == '/':
                result = calc.divide(num1, num2)
            elif operation == '**':
                result = calc.power(num1, num2)
            
            print(f"Result: {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()