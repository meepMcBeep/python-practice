#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

vowels = ['a','e','i','o','u']

def main():
	while True:
		userInput = input("Enter a string: ").strip().lower()
		if userInput:
			break
		else:
			print("Input can not be empty")
	vowelCount = 0
	vowelDictionary = {
		"a": 0,
		"e": 0,
		"i": 0,
		"o": 0,
		"u": 0,
	}
	for character in userInput:
		if character in vowels:
			vowelCount += 1
			vowelDictionary[character] += 1
	print(f"Input: {userInput}")
	print(f"Vowels Found: ")
	for vowel in vowels:
		if vowelDictionary[vowel] > 0:
			print(f"{vowel}: {vowelDictionary[vowel]}")


if __name__ == "__main__":
	main()