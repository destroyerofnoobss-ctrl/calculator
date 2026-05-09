#!/usr/bin/env python3
"""
Simple Calculator - Executable version
A command-line calculator with basic arithmetic operations
"""

import sys
import re

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("         SIMPLE CALCULATOR")
    print("="*40)
    print("Operations:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    print("  % : Modulo")
    print("  ** : Power")
    print("  'quit' or 'exit': Close calculator")
    print("="*40 + "\n")

def validate_expression(expr):
    """Validate the mathematical expression"""
    # Allow only numbers, operators, parentheses, and whitespace
    if not re.match(r'^[\d+\-*/%().\s**]+$', expr):
        return False
    return True

def calculate(expression):
    """Calculate the result of an expression"""
    try:
        if not validate_expression(expression):
            return "Error: Invalid characters in expression"
        
        # Remove whitespace
        expression = expression.replace(" ", "")
        
        if expression == "":
            return "Error: Empty expression"
        
        # Use eval safely with restricted context
        result = eval(expression, {"__builtins__": {}}, {})
        
        # Format the result
        if isinstance(result, float):
            if result.is_integer():
                return int(result)
            else:
                return round(result, 10)  # Limit decimal places
        return result
    
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Invalid syntax"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main calculator loop"""
    display_menu()
    
    while True:
        try:
            user_input = input("Enter expression (or 'quit' to exit): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using Simple Calculator!")
                break
            
            if not user_input:
                print("Please enter an expression\n")
                continue
            
            result = calculate(user_input)
            print(f"\n{user_input} = {result}\n")
        
        except KeyboardInterrupt:
            print("\n\nCalculator closed by user")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
