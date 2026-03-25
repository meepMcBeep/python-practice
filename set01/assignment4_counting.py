#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

"""
Filename: assignment4_counting.py
Author: David Barban
Date: 3/17/2026
Description: This script asks for a positive integer and prints numbers from 1 to N, along with their sum.
"""

def main():
	#print("main")
	while True:
		try:
			user_input = int(input("Please enter a positive integer: "))
			if user_input > 0:
				break
			else:
				print("Please enter a number greater than 0.")
		except ValueError:
			print("Please enter a positive integer!")
	#print(f"{user_input}")

	#counting_sum = 0
	for i in range(1, user_input + 1):
		print(f"{i}")
		#counting_sum += i
	counting_sum = sum(range(1, user_input + 1))
	print(f"Sum: {counting_sum}")

if __name__ == "__main__":
	main()