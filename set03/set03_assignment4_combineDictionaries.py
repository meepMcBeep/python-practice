#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: set03_assignment4_combineDictionaries.py
Author: David Barban
Date: 04-09-2026
Description: combine two given dictionaries into a result dictionary, sum values for matching keys
"""

import random

def create_two_dictionaries():
	key_list = ['a','b','c','d','e']
	new_dict1 = {}
	new_dict2 = {}

	for key in key_list:
		if random.choice([True,False]) == True:
			new_dict1[key] = random.randint(1, 5)
		if random.choice([True,False]) == True:
			new_dict2[key] = random.randint(1, 5)

	return new_dict1, new_dict2

def merge_dictionaries(input_dict1, input_dict2):
	result_dict = {}

	for d in (input_dict1, input_dict2):
	    for key, value in d.items():
	        result_dict[key] = result_dict.get(key, 0) + value

	return result_dict


def main():
	dict1, dict2 = create_two_dictionaries()
	print(f"Dictionary 1: {dict1}")
	print(f"Dictionary 2: {dict2}")

	merged_dict = merge_dictionaries(dict1, dict2)

	print(f"Merged and sorted dictionary: {dict(sorted(merged_dict.items()))}")

if __name__ == "__main__":
	main()