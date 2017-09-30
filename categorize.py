#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse # Reading command line args
import re # Using regex
import os # Manipulating files

# Reading the rules file and returning them in a list  
def read_rules(file):
        patterns = []
        with open(file) as f:
            raw_rules = f.read().splitlines()
            for rule in raw_rules:
                patterns.append(rule.split(";"))
        return patterns

# Categorizing items and writing output in a CSV file
def write_csv(patterns,items,file,sep=";"):
    with open(file, 'w') as output:
        output.write("item" + sep + "category\n") # headings for our CSV file  
        for item in items:
            output.write(item + sep + categorize_item(patterns,item) + "\n")

# Finding the category for a single item  
def categorize_item(patterns,item):
    for (pattern,category) in patterns:
        if re.search(pattern,item) is not None:
            return category
            break
    return "nomatch" # we want to return something anyway



if __name__ == '__main__':
    
    # Let's get those arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--rules', type=str, required=True,
                        help='Rules file (required)')
    parser.add_argument('-i', '--input', type=str, required=True,
                        help="Input file (required)")
    parser.add_argument('-o', '--output', type=str, required=False,
                        help="Output file (default: categorised.csv)", default="categorized.csv")
    parser.add_argument('-s', '--sep', type=str, required=False,
                        help="Output file CSV separator (default: ';' )", default=";")
    args = parser.parse_args()


    # Start by checking if the rules file exists, then read it
    if os.path.exists(args.rules):
        rules = read_rules(args.rules)
    else:
        raise Exception("Rules file does not exist.")

    # Then let's check if the input file exist and read it
    if os.path.exists(args.input):
        with open(args.input) as f:
            items = f.read().splitlines()
    else:
        raise Exception("Input file does not exist.")

    # Finally, we'll write our output file
    write_csv(rules,items,args.output,args.sep)
