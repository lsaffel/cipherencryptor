# Given a non-empty string of lower case letters and a non-negative
# integer representing a key, write a function that returns a new
# string obtained by shifting every letter in the input string
# by k positions in the alphabet, where k is the key
# Note that letters should "wrap" around the alphabet. In other words,
# the letter z shifted by one letter returns the letter a

# sample input:
# string = "zyx"
# key = 2
# sample output:
# "baz"

def caesarCipherEncryptor(string, key):
    new_string = ""
    for charr in range(len(string)):
        char_val = ord(string[charr])
        new_val = char_val + key
        if new_val > ord('z'):
            new_val -= 26
        new_char = chr(new_val)
        new_string += new_char
    return new_string

pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(caesarCipherEncryptor('abc',3))
    print(caesarCipherEncryptor('def',3))
    print(caesarCipherEncryptor('xyz',3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
