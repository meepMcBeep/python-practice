#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

"""
Filename: set02_assignment2_listMinMax.py
Author: David Barban
Date: 3/18/2026
Description: This script iterates through a list of integers and returns the largest and smallest elements
"""

def main():
	numbers = [12, -4, 88, 23, 88, 0, -15, 42, 7, 42]
	if numbers:
		largest = numbers[0]
		smallest = numbers[0]
		for value in numbers[1:]:
			if value > largest:
				largest = value
			if value < smallest:
				smallest = value
		print(f"Largest list element: {largest}")
		print(f"Smallest list element: {smallest}")
	else:
		print("No list given.")

if __name__ == "__main__":
	main()