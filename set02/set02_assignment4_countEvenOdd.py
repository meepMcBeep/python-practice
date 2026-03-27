#! /usr/bin/env python3
#! -*- coding: UTF-8 -*-

"""
Filename: set02_assignment4_countEvenOdd.py
Author: David Barban
Date: 03-27-2026
Description: from a given list of integers, return lists of even and odd numbers
"""

import random


def split_even_odd(numbers):
	even_list = []
	odd_list = []

	for number in numbers:
		if number % 2 == 0:
			even_list.append(number)
		else:
			odd_list.append(number)
	return even_list, odd_list

def main():
	random_list = [random.randint(-100, 100) for _ in range(10)]

	even_list, odd_list = split_even_odd(random_list)

	print(f"Original list: {random_list}")
	print(f"Odd list: {odd_list}")
	print(f"Even list: {even_list}")

if __name__ == "__main__":
	main()