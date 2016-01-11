#!/usr/bin/env python3
import hashlib
import re


def make_hash(letter):
    code = str(hashlib.md5(letter).hexdigest())[0:6]
    return code


# TODO ignore non-letter characters
if __name__ == "__main__":
    characters = str(input("'Feed me string' - Nyan Cat:\n"))
    characters = re.sub('[^0-9a-zA-Z]+', '', characters)
    print(characters)
    hashes = []
    for letter in characters:
        code = "#" + make_hash(letter.encode('utf-8'))
        hashes.append(code)
    print(hashes)
