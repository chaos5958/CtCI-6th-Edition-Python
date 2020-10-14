import unittest

def string_compression(string):
    string_counter = []
    count = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i-1]:
            string_counter += string[i-1] + str(count)
            count = 1
        else:
            count += 1

    string_counter += string[-1] + str(count)

    return min(''.join(string_counter), string, key=len)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
