import unittest

def is_unique(string):
    if len(string) > 128:
        return True

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val] is False:
            char_set[val] = True
        else:
            return False

    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        for test_string in self.dataT:
            result = is_unique(test_string)
            self.assertTrue(result)
        for test_string in self.dataF:
            result = is_unique(test_string)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
