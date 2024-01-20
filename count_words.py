import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Find the number of words from a Latex text.')
    parser.add_argument('-str', help='Input string', nargs='?', type=str, const=None)

    args = parser.parse_args()

    if not args.str:
        print("Ask for help. -h or --h")
        return
    
    input = sys.argv[1]
    index = input.find("\citet")
    while index != -1:
        input = input[:index - 1] + input[index + 6 :]
        index = input.find("citet")

    start_index = input.find("{")
    end_index = input.find("}")

    while start_index != -1 and end_index != -1:
        input = input[:start_index - 1] + input[end_index + 1:]
        start_index = input.find("{")
        end_index = input.find("}")

    words = input.split(" ")
    print(f"\nInput string has: {len(words)} words.\n") 


if __name__ == '__main__':
    main();
