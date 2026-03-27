#! /usr/bin/env python3
#! -*- coding: UTF-8 -*-

"""
Filename: set02_assignment4_countEvenOdd.py
Author: David Barban
Date: 03-27-2026
Description: from a given list of integers, return lists of even and odd numbers
"""
import random

global_random_list = [random.randint(-100, 100) for number in range(10)]

def main():
	odd_list = []
	even_list = []

	for number in global_random_list:
		if number % 2 == 0:
			even_list.append(number)
		else:
			odd_list.append(number)

	print(f"Original list: {global_random_list}")
	print(f"Odd list: {odd_list}")
	print(f"Even list: {even_list}")

if __name__ == "__main__":
	main()