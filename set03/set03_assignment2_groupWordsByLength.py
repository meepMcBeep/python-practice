#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

"""
Filename: set03_assignment2_groupWordsByLength.py
Author: David Barban
Date: 03-31-2026
Description: Given an input string return words grouped by length
"""

def group_words_by_length(sentence):
	words_dict = {}

	for word in sentence.lower().split():
		length = len(word)
		if length not in words_dict:
			words_dict[length] = []
		words_dict[length].append(word)

	for key in words_dict:
		words_dict[key] = sorted(words_dict[key])

	return words_dict

def main():
	while True:
		input_sentence = input("Enter a sentence of words, and I will alphabetically return the words grouped by length: ").strip()
		if input_sentence:
			break
		print("Input cannot be empty.")

	print(group_words_by_length(input_sentence))


if __name__ == "__main__":
	main()