#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: set03_assignment3_firstNonRecurringCharacter.py
Author: David Barban
Date: 04-07-2026
Description: Return the first non-repeating character from an input string
"""

def build_dict_from_string(some_string):
	new_dict = {}
	for character in some_string:
		new_dict[character] = new_dict.get(character, 0) + 1
	return new_dict

def find_non_repeating_characters(some_string, some_dict):
	for character in some_string:
		if some_dict[character] == 1:
			return character
	return None

def main():
	while True:
		input_string = input("Enter a string and I will return the first non-repeating character: " ).lower()
		if input_string.strip() != "":
			break
		print("Enter a non-empty string")
	#print(f"{input_string}")

	char_dict = build_dict_from_string(input_string)

	first_non_repeating_char = find_non_repeating_characters(input_string, char_dict)
	if first_non_repeating_char is None:
		print("No non-repeating character found.")
	else:
		print(f"First non-repeating character is '{first_non_repeating_char}'")


if __name__ == "__main__":
	main()