import sys
import argparse

# How to use it?
# python count_words.py -str=input_string

# Example: python count_words.py -str='Hello!'

def main():
    parser = argparse.ArgumentParser(description='Find the number of words from a Latex text.')
    parser.add_argument('-str', help='Input string', nargs='?', type=str, const=None)

    args = parser.parse_args()

    if not args.str:
        print("Ask for help. -h or --h")
        return
    
    input = args.str
    index = input.find("\citet")
    while index != -1:
        input = input[:index - 1] + input[index + 6 :]
        index = input.find("\citet")

    start_index = input.find("{")
    end_index = input.find("}")

    while start_index != -1 and end_index != -1:
        input = input[:start_index] + input[end_index + 1:]
        start_index = input.find("{")
        end_index = input.find("}")

    print(input)
    words = input.split(" ")
    print(f"\nInput string has: {len(words)} words.\n") 


if __name__ == '__main__':
    main();
