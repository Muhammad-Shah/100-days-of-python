# Calculator
from art import logo
import os
clear = lambda:os.system('cls')
# Addition
def add(n1, n2):
    return n1+n2
# Subtraction
def subtract(n1, n2):
    return n1-n2
# Product
def multiply(n1, n2):
    return n1*n2
# Division
def divide(n1, n2):
    return n1/n2

# Dictionary
operation = {
 "+":add,
 "-":subtract,
 "*":multiply,
 "/":divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number: "))
    for operator in operation:
        print(operator)    # Print all operators(Keys)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation symbol frm the line above: ")
        num2 = float(input("What's the next number: "))
        calculation_functiion = operation[operation_symbol]  # Based on the key(operation_symbol) a value(function) from the dictionary will be selected
        answer = calculation_functiion(n1=num1, n2=num2) # Then function will return value and stored in answer
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculation with the {answer}:Type 'n' to start new calculation ") == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()

calculator()