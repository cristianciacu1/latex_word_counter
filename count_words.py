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

    name_followed_by_curly_braces = ['\citet', '\citep', '\cite']

    for keyword in name_followed_by_curly_braces:
        index = input.find(keyword)
        while index != -1:
            input = input[:index - 1] + input[index + len(keyword) :]

            start_index = input.find("{")
            end_index = input.find("}")
            
            if (start_index == -1 and end_index != -1) or (start_index != -1 and end_index == -1):
                print("There is a pair of {} which is not complete.")
                return
    
            input = input[:start_index] + input[end_index + 1:]

            index = input.find(keyword)

    words = input.split(" ")
    counter = 0
    for word in words:
        if word:
            counter += 1

    print(f"\nInput string has: {counter} words.\n") 


if __name__ == '__main__':
    main();
