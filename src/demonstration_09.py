"""
Challenge #9:

Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter, respectively.

Examples:
- mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
- mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
- mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

Notes:
- All of the letters in the input list will always be lowercase.
"""
def mapping(letters):
    letter_dict = {}
    
    for letter in letters:
        # add a new key value to the dictionary
        # where the key is the letter and
        # the value is the Capitalized version of the letter
        letter_dict[letter] = letter.upper()
    return letter_dict

print( mapping(["a", "v", "y", "z"]))

