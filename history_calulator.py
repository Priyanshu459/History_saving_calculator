import os

HISTORY_FILE = "history.txt"

def show_history():
    if not os.path.exists(HISTORY_FILE) or os.path.getsize(HISTORY_FILE) == 0:
        print("No history found!")
        return
    with open(HISTORY_FILE, 'r') as file:
        lines = file.readlines()
        for line in reversed(lines):
            print(line.strip())

def clear_history():
    open(HISTORY_FILE, 'w').close()
    print("History cleared")

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    try:
        parts = user_input.strip().split()
        if len(parts) != 3:
            print("Invalid input format. Use: number operator number")
            return

        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Unsupported operator. Use one of +, -, *, /.")
            return

        result = int(result) if result.is_integer() else result
        print("Result:", result)
        save_to_history(user_input, result)

    except ValueError:
        print("Invalid numbers. Please enter valid numeric values.")

def main():
    print("Welcome to the History Saving Calculator!")
    while True:
        user_input = input(
            "Enter calculation (e.g., 2 + 2), 'history' to view history, 'clear' to clear history, or 'exit' to quit: "
        ).strip()

        command = user_input.lower()
        if command == "exit":
            print("GOODBYE")
            break
        elif command == "history":
            show_history()
        elif command == "clear":
            clear_history()
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()