import unittest


def is_substring(string, sub):
    return string.find(sub) != -1

def string_rotation(str1, str2):
    if len(str1) == len(str2) != 0:
        return is_substring(str1 + str1, str2)
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
