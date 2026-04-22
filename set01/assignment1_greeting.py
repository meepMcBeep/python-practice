#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: assignment1_greeting.py
Author: David Barban
Date: 2026-03-11
Description: This script asks for a user's name and age, then prints their age next yeasr and in five years.
"""

# Your code starts here, after the header and docstring
#import sys - not used
#testing from new machine

def main():
    name = input("What is your name? ")
    while True:
        try:
            age = int(input("What is your age? "))
            if age >= 0:
                break
            print("Please enter a non-negeative integer for age")
        except ValueError:
            print("Invalid Age Input! Please enter an integer")
    print(f"Hello, {name}!")
    print(f"Next year you will be {age+1} years old.")
    print(f"In five years you will be {age+5} years old.")

if __name__ == "__main__":
    main()