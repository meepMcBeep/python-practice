#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

"""
Filename: set02_assignment3_countVowelsInString.py
Author: David Barban
Date: 03/26/2026
Description: Ask the user for an input string and return the total count and individual counts of vowels in the string
"""

vowels = {'a', 'e', 'i', 'o', 'u'}

def main():
	while True:
		user_input = input("Enter a string: ").strip().lower()
		if user_input:
			break
		print("Input cannot be empty")

	vowel_count = 0
	vowel_dictionary = {vowel: 0 for vowel in vowels}

	for character in user_input:
		if character in vowels:
			vowel_count += 1
			vowel_dictionary[character] += 1

	print(f"Input: {user_input}")
	print(f"Total Vowels: {vowel_count}")
	print("Vowels Found:")
	
	for vowel in sorted(vowels):
		if vowel_dictionary[vowel] > 0:
			print(f"{vowel}: {vowel_dictionary[vowel]}")


if __name__ == "__main__":
	main()