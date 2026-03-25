#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

"""
Filename: assignment5_basicCalculator.py
Author: David Barban
Date: 3/17/2026
Description: This Script asks a user for two integers and a calculation operation and returns the result
"""

def add(addend_1, addend_2):
	return addend_1 + addend_2

def subtract(minuend, subtrahend):
	return minuend - subtrahend

def multiply(multiplacand, multiplier):
	return multiplacend * multiplier

def divide(dividend, divisor):
	if divisor == 0:
		return None
	else:
		return dividend / divisor

def main():
	allowed_operations = {'+', '-', '*', '/'}
	print("Enter two numbers and an operation")
	while True:
		try:
			number_input1 = float(input("Enter first number: "))
			number_input2 = float(input("Enter second number: "))
			operation_selection = input("Choose operation (+, -, *, /): ")
			if operation_selection in allowed_operations:
				break
			else:
				print("Please select a valid operation")
		except ValueError:
			print("Please enter valid numbers")
	if operation_selection == "+":
		result = add(number_input1, number_input2)
	elif operation_selection == "-":
		result = subtract(number_input1, number_input2)
	elif operation_selection == "*":
		result = multiply(number_input1, number_input2)
	else:
		result = divide(number_input1, number_input2)
	if result is None:
		print("Error: Division by zero")
	else:
		print(f"Result: {result}")


if __name__ == "__main__":
	main()