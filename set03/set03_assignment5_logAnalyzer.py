#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: set03_assignment5_logAnalyzer.py
Author: David Barban
Date: 04-09-2026   
Description: analyze a log file and print the number of occurrences of each log level
"""
import random

def generate_sample_log_file():
    #define a set of possible entries
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]

    #create a log file of random length with random log levels
    with open("log.txt", "w") as log_file:
        for _ in range(random.randint(50, 100)):
            log_file.write(f"{log_levels[random.randrange(len(log_levels))]}\n")
    
    #return the log file name
    return "log.txt"


def count_log_levels(log_file):
    log_counts = {}

    #count the occurrences of each log level in the log file
    with open(log_file, "r") as file:
        for line in file:
            log_level = line.strip()
            log_counts[log_level] = log_counts.get(log_level, 0) + 1

    #print the counts of each log level
    for log_level, count in sorted(log_counts.items()):
        print(f"{log_level}: {count}")

    #find most frequent log level
    most_frequent_log_level = max(log_counts, key=log_counts.get)
    print(f"Most Frequent Log Level: {most_frequent_log_level}")

def main():
    log_file = generate_sample_log_file()
    count_log_levels(log_file)

if __name__ == "__main__":
    main()