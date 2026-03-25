#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

"""
Filename: assignment3_scoreGrading.py
Author: David Barban
Date: 3/17/2026
Description: Ask user to input a score 0-100 and return the corresonding letter grade
"""

def main():
	while True:
		try:
			score_input = int(input("Enter a score 0-100: "))
			if( 0 <= score_input <= 100):
				break
		except ValueError:
			print("Enter an integer score between 0-100")
	#print(score_input)

	"""
	#remove unneeded parentheses, don't single line, avoid redudant lower bounds
	if 0 <=score_input < 60: print("Grade: F")
	elif (60 <= score_input < 70): print("Grade: D")
	elif (70 <= score_input < 80): print("Grade: C")
	elif (80 <= score_input < 90): print("Grade: B")
	else: print("Grade: A")
	"""

	if score_input < 60:
		grade = "F"
	elif score_input < 70:
		grade = "D"
	elif score_input < 80:
		grade = "C"
	elif score_input < 90:
		grade = "B"
	else:
		grade = "A"

	print(f"Grade: {grade}")

if __name__ == "__main__":
	main()