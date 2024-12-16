#!/usr/bin/env python3

def main():
    path_to_file = "books/frankenstein.txt"
    contents = open_and_read(path_to_file)
    words = count_words(contents)
    chars = count_chars(contents)
    print(f"{words} words in here")
    print("======================")
    print("individual character count:")
    for char, count in chars.items():
        print(f"'{char}':    {count}")


def open_and_read(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
        return contents


def count_words(text):
    words = text.split()
    count = len(words)
    return count


def count_chars(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict.update({char: 1})
        else:
            char_dict[char] += 1

    return char_dict


main()

