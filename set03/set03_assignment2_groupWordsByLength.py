#! /usr/bin/env python3
#! -*- Coding utf-8 -*-

"""
Filename: set03_assignment2_groupWordsByLength.py
Author: David Barban
Date: 03-31-2026
Description: Given an input string return words grouped by length
"""

def group_words_by_length(sentence):
	words_dict = {}
	for word in sentence.lower().split():
		if words_dict.get(len(word)) is None:
			words_dict[len(word)] = [word]
		elif word not in words_dict[len(word)]:
			words_dict[len(word)].append(word)

	for key, value in words_dict.items():
		words_dict[key] = sorted(words_dict[key])

	return words_dict

def main():
	while True:
		input_sentence = input("Enter a sentence of words, and I will alphabetically return the words grouped by length: ")
		if input_sentence:
			break
		else:
			print("Input cannot be empty")

	print(f"{group_words_by_length(input_sentence)}")


if __name__ == "__main__":
	main()