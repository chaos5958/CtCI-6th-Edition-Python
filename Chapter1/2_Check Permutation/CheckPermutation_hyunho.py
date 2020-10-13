import unittest
from collections import Counter

def check_permutation(string1, string2):
    char_count1 = [0 for _ in range(128)]
    char_count2 = [0 for _ in range(128)]

    for char1, char2 in zip(string1, string2):
        char_count1[ord(char1)] += 1
        char_count2[ord(char2)] += 1

    for val1, val2 in zip(char_count1, char_count2):
        if val1 != val2:
            return False

    return True

def check_permutation_optimized(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        for test_strings in self.dataT:
            result = check_permutation_optimized(*test_strings)
            self.assertTrue(result)
        for test_strings in self.dataF:
            result = check_permutation_optimized(*test_strings)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
