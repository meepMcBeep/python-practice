#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: assignment2_evenOdd.py
Author: David Barban
Date: 3-12-2026
Description: This script asks the user for an integer and prints whether it is even or odd.
"""

def main():
	#print("this is main")
	while True:
		try:
			user_input = int(input("Enter an integer number: "))
			break
		except ValueError:
			print("Invalid input. Please enter an integer number.")
	"""
	print(f"The number is {userInput}.")
	if(userInput % 2 ==0):
		print("even")
	else:
		print("odd")
	"""
	results = "Even" if user_input % 2 == 0 else "Odd"
	print(f"{user_input} is {results}")
	#print(str(user_input) + " is " + results + ".")


if __name__ == "__main__":
	main()