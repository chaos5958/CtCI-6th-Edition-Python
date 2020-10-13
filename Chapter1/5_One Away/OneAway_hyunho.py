import unittest

def one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i] and i != len(str1) - 1:
                return str1[i+1:len(str1)] == str2[i+1:len(str1)]
    else:
        if len(str1) > len(str2):
            longer_str = str1
            shorter_str = str2
        else:
            longer_str = str2
            shorter_str = str1

        for i in range(len(shorter_str)):
            if shorter_str[i] != longer_str[i]:
                return shorter_str[i:len(shorter_str)] == longer_str[i+1:len(shorter_str)+1]

    return True

def one_away(s1, s2):
    '''Check if a string can converted to another string with a single edit'''
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    return False


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
