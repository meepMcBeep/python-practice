#! /usr/bin/env python3
#! -*- Coding: utf-8

"""
Filename: set03_assignment1_findDuplicates.py
Author: David Barban
Date: 03/31/2026
Description: From a list of integers, return a list of duplicates
"""

import random

def create_random_list(min_val,max_val,list_size):
	new_list = [random.randint(min_val,max_val) for _ in range(list_size)]
	return new_list

def identify_duplicates(input_list):
	seen_numbers = []
	identified_duplicates = set()

	for number in input_list:
		if number in seen_numbers:
			identified_duplicates.add(number)
		else:
			seen_numbers.append(number)
			
	return identified_duplicates


def main():
	list_of_numbers = create_random_list(1,10,10)
	print(f"list of numbers: {list_of_numbers}")
	print(f"list_of_duplicates: {identify_duplicates(list_of_numbers)}")


if __name__ == "__main__":
	main()