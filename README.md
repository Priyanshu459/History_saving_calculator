# History_saving_calculator
# History Saving Calculator 🧮📝

A command-line calculator that performs basic arithmetic operations and automatically saves all calculations to a file for future reference. Perfect for keeping track of your calculations and reviewing past work!

## 🌟 Features

- ➕ Basic arithmetic operations (addition, subtraction, multiplication, division)
- 💾 Automatic calculation history saving
- 📜 View past calculations in reverse chronological order
- 🗑️ Clear history when needed
- ⚠️ Error handling for invalid inputs and division by zero
- 🎯 Simple, intuitive command-line interface
- 📁 Persistent storage across sessions

## 📋 Prerequisites

- Python 3.7 or higher
- No external libraries required (uses only Python's built-in modules)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/history-calculator.git
cd history-calculator
```

### 2. Run the Calculator

```bash
python history_calculator.py
```

That's it! No dependencies to install. 🎉

## 💻 Usage

### Starting the Calculator

```bash
python history_calculator.py
```

### Basic Operations

Enter calculations in the format: `number operator number`

```
Enter calculation: 5 + 3
Result: 8

Enter calculation: 10 - 4
Result: 6

Enter calculation: 7 * 8
Result: 56

Enter calculation: 20 / 4
Result: 5
```

### View History

```
Enter calculation: history

20 / 4 = 5
7 * 8 = 56
10 - 4 = 6
5 + 3 = 8
```

### Clear History

```
Enter calculation: clear
History cleared
```

### Exit Calculator

```
Enter calculation: exit
GOODBYE
```

## 🎯 Supported Operations

| Operator | Operation      | Example  | Result |
|----------|---------------|----------|--------|
| `+`      | Addition      | `5 + 3`  | `8`    |
| `-`      | Subtraction   | `10 - 4` | `6`    |
| `*`      | Multiplication| `7 * 6`  | `42`   |
| `/`      | Division      | `20 / 5` | `4`    |

## 📁 Project Structure

```
history-calculator/
│
├── history_calculator.py    # Main application file
├── history.txt             # Auto-generated history file
├── README.md              # This file
├── LICENSE                # MIT License
├── .gitignore            # Git ignore file
│
└── tests/                # Unit tests (optional)
    └── test_calculator.py
```

## 🎨 Sample Session

```
Welcome to the History Saving Calculator!

Enter calculation (e.g., 2 + 2), 'history' to view history, 'clear' to clear history, or 'exit' to quit: 10 + 5
Result: 15

Enter calculation (e.g., 2 + 2), 'history' to view history, 'clear' to clear history, or 'exit' to quit: 20 * 3
Result: 60

Enter calculation (e.g., 2 + 2), 'history' to view history, 'clear' to clear history, or 'exit' to quit: 100 / 4
Result: 25

Enter calculation (e.g., 2 + 2), 'history' to view history, 'clear' to clear history, or 'exit' to quit: history
100 / 4 = 25
20 * 3 = 60
10 + 5 = 15

Enter calculation (e.g., 2 + 2), 'history' to view history, 'clear' to clear history, or 'exit' to quit: exit
GOODBYE
```

## ⚠️ Error Handling

### Division by Zero
```
Enter calculation: 10 / 0
Error: Division by zero is not allowed.
```

### Invalid Format
```
Enter calculation: 5+3
Invalid input format. Use: number operator number
```

### Invalid Numbers
```
Enter calculation: abc + 5
Invalid numbers. Please enter valid numeric values.
```

### Unsupported Operator
```
Enter calculation: 5 % 3
Unsupported operator. Use one of +, -, *, /.
```

## 🛠️ Enhanced Features

### Version 2.0 - Advanced Calculator

Here's an enhanced version with more features:

```python
import os
from datetime import datetime
import math

HISTORY_FILE = "history.txt"

class AdvancedCalculator:
    def __init__(self):
        self.history = []
        self.load_history()
    
    def load_history(self):
        """Load history from file on startup"""
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r') as f:
                self.history = [line.strip() for line in f.readlines()]
    
    def show_history(self, limit=None):
        """Show calculation history"""
        if not self.history:
            print("📭 No history found!")
            return
        
        print("\n📜 Calculation History:")
        print("=" * 50)
        
        display_history = self.history[-limit:] if limit else self.history
        for i, line in enumerate(reversed(display_history), 1):
            print(f"{i}. {line}")
        print("=" * 50)
    
    def clear_history(self):
        """Clear all history"""
        open(HISTORY_FILE, 'w').close()
        self.history = []
        print("🗑️  History cleared successfully!")
    
    def save_to_history(self, equation, result):
        """Save calculation to history"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {equation} = {result}"
        
        with open(HISTORY_FILE, 'a') as file:
            file.write(f"{entry}\n")
        
        self.history.append(entry)
    
    def calculate_basic(self, num1, op, num2):
        """Perform basic arithmetic operations"""
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else None,
            '^': lambda x, y: x ** y,
            '%': lambda x, y: x % y if y != 0 else None,
        }
        
        if op not in operations:
            return None, f"Unsupported operator. Use one of: {', '.join(operations.keys())}"
        
        if op in ['/', '%'] and num2 == 0:
            return None, "Error: Division by zero is not allowed."
        
        result = operations[op](num1, num2)
        return result, None
    
    def calculate_advanced(self, expression):
        """Handle advanced operations"""
        expr = expression.lower().strip()
        
        # Square root
        if expr.startswith('sqrt'):
            try:
                num = float(expr.replace('sqrt', '').strip())
                if num < 0:
                    return None, "Error: Cannot calculate square root of negative number"
                return math.sqrt(num), None
            except:
                return None, "Invalid sqrt format. Use: sqrt 16"
        
        # Power
        elif 'pow' in expr:
            try:
                parts = expr.replace('pow', '').strip().split()
                base, exp = float(parts[0]), float(parts[1])
                return base ** exp, None
            except:
                return None, "Invalid pow format. Use: pow 2 3"
        
        return None, "Unknown advanced operation"
    
    def calculate(self, user_input):
        """Main calculation handler"""
        try:
            # Check for advanced operations
            if any(word in user_input.lower() for word in ['sqrt', 'pow']):
                result, error = self.calculate_advanced(user_input)
                if error:
                    print(f"❌ {error}")
                    return
                print(f"✅ Result: {result}")
                self.save_to_history(user_input, result)
                return
            
            # Basic operations
            parts = user_input.strip().split()
            if len(parts) != 3:
                print("❌ Invalid input format. Use: number operator number")
                return

            num1 = float(parts[0])
            op = parts[1]
            num2 = float(parts[2])

            result, error = self.calculate_basic(num1, op, num2)
            
            if error:
                print(f"❌ {error}")
                return
            
            # Format result
            result = int(result) if result.is_integer() else round(result, 4)
            print(f"✅ Result: {result}")
            self.save_to_history(user_input, result)

        except ValueError:
            print("❌ Invalid numbers. Please enter valid numeric values.")
        except Exception as e:
            print(f"❌ An error occurred: {e}")
    
    def show_help(self):
        """Display help information"""
        help_text = """
╔══════════════════════════════════════════════════════════╗
║           CALCULATOR HELP & COMMANDS                      ║
╚══════════════════════════════════════════════════════════╝

📊 BASIC OPERATIONS:
   Addition:       5 + 3
   Subtraction:    10 - 4
   Multiplication: 7 * 6
   Division:       20 / 5
   Power:          2 ^ 3
   Modulo:         10 % 3

🔬 ADVANCED OPERATIONS:
   Square Root:    sqrt 16
   Power:          pow 2 3

📜 COMMANDS:
   history [n]  - View last n calculations (or all if n not specified)
   clear        - Clear all history
   help         - Show this help message
   exit         - Exit calculator

💡 TIPS:
   - Use spaces between numbers and operators
   - History is saved automatically
   - Results are rounded to 4 decimal places
        """
        print(help_text)
    
    def run(self):
        """Main calculator loop"""
        print("╔══════════════════════════════════════════════════════════╗")
        print("║     🧮 HISTORY SAVING CALCULATOR v2.0                    ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print("\nType 'help' for commands and usage information.\n")
        
        while True:
            user_input = input("🔢 Enter calculation: ").strip()
            
            if not user_input:
                continue
            
            command = user_input.lower().split()[0]
            
            if command == "exit":
                print("\n👋 GOODBYE! Thanks for using the calculator!")
                break
            elif command == "history":
                parts = user_input.split()
                limit = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else None
                self.show_history(limit)
            elif command == "clear":
                self.clear_history()
            elif command == "help":
                self.show_help()
            else:
                self.calculate(user_input)

if __name__ == "__main__":
    calculator = AdvancedCalculator()
    calculator.run()
```

## 🎓 Code Features Explained

### File Handling
```python
# Check if file exists and has content
if not os.path.exists(HISTORY_FILE) or os.path.getsize(HISTORY_FILE) == 0:
    print("No history found!")
```

### Display in Reverse Order
```python
# Show newest calculations first
for line in reversed(lines):
    print(line.strip())
```

### Clean Integer Display
```python
# Display 5 instead of 5.0
result = int(result) if result.is_integer() else result
```

## 🧪 Testing

Create `tests/test_calculator.py`:

```python
import unittest
import os
from history_calculator import calculate, save_to_history, show_history

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_history.txt"
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_addition(self):
        # Test would go here
        pass
    
    def test_division_by_zero(self):
        # Test would go here
        pass

if __name__ == '__main__':
    unittest.main()
```

## 📝 .gitignore

Create a `.gitignore` file:

```gitignore
# History files
history.txt
test_history.txt
*.txt

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
.coverage
htmlcov/
```

## 🚀 Future Enhancements

### Planned Features
- [ ] Scientific calculator functions (sin, cos, tan, log)
- [ ] Support for complex expressions (e.g., `(5 + 3) * 2`)
- [ ] Export history to CSV/Excel
- [ ] Statistics on calculations (most used operations, averages)
- [ ] GUI version using Tkinter
- [ ] Web version using Flask
- [ ] Memory storage (M+, M-, MR, MC)
- [ ] Unit conversions
- [ ] Date/time filtering for history
- [ ] Search functionality in history

### Community Ideas
- Graphing capabilities
- Equation solver
- Matrix operations
- Currency conversion
- Programmer mode (binary, hex, octal)

## 🐛 Troubleshooting

### Issue: History file not saving
**Solution:** Check write permissions in the directory

### Issue: History shows in wrong order
**Solution:** The newest calculations should appear first. Update to latest version.

### Issue: Decimal places too long
**Solution:** Use the enhanced version with rounding feature

### Issue: Can't perform multiple operations
**Solution:** For complex expressions like `(5+3)*2`, calculate step by step or use the enhanced version

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/scientific-calc`)
3. Implement your feature with tests
4. Commit your changes (`git commit -m 'Add scientific functions'`)
5. Push to the branch (`git push origin feature/scientific-calc`)
6. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions
- Include unit tests for new features
- Update README with new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Built for learning Python file I/O operations
- Inspired by the need for a simple calculation tracker
- Thanks to all contributors and users
- Special thanks to the Python community

## 📚 Learning Resources

- [Python File I/O Documentation](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python os Module](https://docs.python.org/3/library/os.html)
- [Exception Handling in Python](https://docs.python.org/3/tutorial/errors.html)

## 💡 Use Cases

- 📊 **Students**: Track homework calculations
- 💼 **Professionals**: Keep financial calculations
- 🏠 **Personal**: Budget tracking and bill splitting
- 🎓 **Education**: Learn Python file handling
- 📈 **Analysis**: Review calculation patterns

## ⭐ Star This Repo!

If you find this calculator useful, please give it a ⭐ on GitHub!

## 📞 Support

Need help or have questions?
- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/history-calculator/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/history-calculator/discussions)

---

**Made with ❤️ and Python 🐍**

**Happy Calculating! 🧮✨**
