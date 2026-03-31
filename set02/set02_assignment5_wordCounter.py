#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

"""
Filename: set02_assignment5_wordCounter.py
Author: David Barban
Date: 03-30-2026
Description: Ask the user for a sentence and return the count of each word
"""

def dictionary_from_sentence(sentence):
	words_dict = {}
	for word in sentence.split():
		if words_dict.get(word) is None:
			words_dict[word] = 1
		else:
			words_dict[word] += 1
	return words_dict


def main():
	#print("main")

	while True:
		user_sentence = input("Enter a sentence, and I will count the instances of each word: ")
		if user_sentence:
			break
		print("Input can not be empty")

	result_dict = dictionary_from_sentence(user_sentence)
	for word in result_dict:
		print(f"{word} occurs {result_dict[word]} times")

if __name__ == "__main__":
	main()