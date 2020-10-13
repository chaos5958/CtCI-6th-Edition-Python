import unittest
from collections import Counter

#TODO: count (upper-, lower-)
#TODO: check (odd: one)

def check_palindrome(string):
    char_count = Counter()
    for char in string:
        number = char_to_number(char)
        if number != -1:
            char_count[number] += 1

    odd_count = 0
    for key in char_count:
        if char_count[key] % 2 == 1:
            odd_count += 1
            if odd_count == 2:
                return False

    return True

def check_palindrome_optimized(phrase):
    '''function checks if a string is a permutation of a palindrome or not'''
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1

    return countodd <= 1

def char_to_number(char):
    num_a = ord('a')
    num_z = ord('z')
    num_A = ord('A')
    num_Z = ord('Z')
    num_char = ord(char)

    if num_a <= num_char <= num_z:
        return ord(char) - num_a
    if num_A <= num_char <= num_Z:
        return ord(char) - num_A

    return -1

class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_cp(self):
        for [test_string, expected] in self.data:
            actual = check_palindrome(test_string)
            self.assertEqual(actual, expected)

if __name__  == '__main__':
    unittest.main()
