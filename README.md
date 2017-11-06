# Categorize

Small Python script to categorize data using RegEx.  


## Install

Simply clone this repo:  

    git clone git@gitlab.com:databulle/categorize.git  


## Use

You'll need:  
- A file containing the rules you want to apply (see syntax below),  
- A file containing the items you want to categorize (one item per line).  

It's quite simple:  

    python categorize.py -r example-rules.txt -i example-data.csv  

Default outputs to a CSV file with semicolon separator: `categorized.csv`.  


Command line arguments:  
- `-h`, `--help` shows help message and exits  
- `-r RULES`, `--rules RULES` indicates rules file (required)  
- `-i INPUT`, `--input INPUT` indicates input file (required)  
- `-o OUTPUT`, `--output OUTPUT` indicates output file (optional, default: `categorized.csv`)  
- `-s SEP`, `--sep SEP` indicates output file CSV separator (optional, default: `;` )  


## Rules syntax

This script uses standard Python RegEx syntax, and associates each pattern with a category name.  
Each line must start with the regular expression pattern, followed by a semicolumn, and end with the category name:  

    REGEX;CATEGORY_NAME  

You'll find some examples in the `example-rules.txt` file.  
