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
		words_dict[word] = words_dict.get(word, 0) + 1
	return words_dict


def main():
	#print("main")

	while True:
		user_sentence = input("Enter a sentence, and I will count the instances of each word: ")
		if user_sentence:
			break
		print("Input cannot be empty")

	user_sentence = user_sentence.lower()
	result_dict = dictionary_from_sentence(user_sentence)
	for word, count in sorted(result_dict.items()):
   		print(f"{word} occurs {count} times")

if __name__ == "__main__":
	main()