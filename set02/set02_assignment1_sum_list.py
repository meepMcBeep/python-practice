#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

"""
Filename: week2_assignment1_listAccumulator.py
Author: David Barban
Date: 3/18/2026
Description: This script iterates through a list of integers and returns the sum and average of the list
"""

def main():
	numbers = [4, 7, 2, 9, 1]
	list_sum = 0
	for i in numbers:
		list_sum += i
	print(f"Total: {list_sum}")
	if numbers:
		print(f"Average: {list_sum / len(numbers)}")

if __name__ == "__main__":
	main()