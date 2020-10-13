import unittest

def urlify(string, length):
    curr_length = length

    for idx in reversed(range(length)):
        if string[idx] == ' ':
            string[idx+3:curr_length+2] = string[idx+1:curr_length]
            string[idx:idx+3] = "%20"
        curr_length += 2
        idx -= 1

    return string

class Test(unittest.TestCase):
    test_data = (
        (list("Mr John Smith"), 13, list("Mr%20John%20Smith")),
         )

    def test_rb(self):
        for input_str, length, expected_str in self.test_data:
            output_str = urlify(input_str, length)
            self.assertEqual(expected_str, output_str)


if __name__ == '__main__':
    unittest.main()
