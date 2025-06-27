#Aaron Truong
# Lab 8 CIS 247 C

"""
Write a Python program that reads a text file (quote.txt) 
Creates a dictionary where each key is a unique word from the file
The value is a list of line numbers where that word appears.
"""

def read_quote_file(filename):
    word_dict = {}
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                words = line.strip().split()
                for word in words:
                    word = word.lower()
                    if word not in word_dict:
                        word_dict[word] = []
                    word_dict[word].append(line_number)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return word_dict

def print_word_occurrences(word_dict):
    for word, lines in word_dict.items():
        print(f"{word} {' '.join(map(str, lines))}")

def main():
    filename = "data\\quote.txt"
    word_dict = read_quote_file(filename)
    print_word_occurrences(word_dict)

main()