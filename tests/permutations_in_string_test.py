import unittest
from src import permutations_in_string as pis


class PermutationsInStringTest(unittest.TestCase):
    def test_permutations_in_string_true(self):
        s1 = "ab"
        s2 = "eidbaooo"
        result = pis.check_inclusion(s1, s2)
        self.assertEqual(True, result)

    def test_permutations_in_string_false(self):
        s1 = "ab"
        s2 = "eidboaoo"
        result = pis.check_inclusion(s1, s2)
        self.assertEqual(False, result)

    def test_permutations_in_string_longer(self):
        s1 = "abdsfgsfd"
        s2 = "abs"
        result = pis.check_inclusion(s1, s2)
        self.assertEqual(False, result)

    def test_permutations_in_string_same_len(self):
        s1 = "abs"
        s2 = "abs"
        result = pis.check_inclusion(s1, s2)
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
