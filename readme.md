# Word counter for Latex
This program is intended to count the words from a Latex document, while ignoring the citations.

## How to run the program
1. See possible options: python count_words.py -h
2. Run the program with an input: python count_words.py -str='your input'

## Limitations
The program does not consider the following commands when counting the number of words: '\cite', '\citep', '\citet'.
