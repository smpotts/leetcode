import unittest
from src import questions as q


class QuestionsTest(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(q.two_sum(nums=[2,7,11,15], target=9), [0, 1])
        self.assertEqual(q.two_sum(nums=[3,2,4], target=6), [1, 2])
        self.assertEqual(q.two_sum(nums=[3,3], target=6), [0, 1])

    def test_is_palindrome(self):
        self.assertEqual(q.is_palindrome(121), True)
        self.assertEqual(q.is_palindrome(-121), False)
        self.assertEqual(q.is_palindrome(123), False)
        self.assertEqual(q.is_palindrome(10), False)
        self.assertEqual(q.is_palindrome(1234321), True)

    def test_remove_duplicates(self):
        self.assertEqual(q.remove_duplicates([1,1,2]), 2)
        self.assertEqual(q.remove_duplicates([0,0,1,1,1,2,2,3,3,4]), 5)

    def test_longest_common_prefix(self):
        self.assertEqual(q.longest_common_prefix(["flower", "flow"]), "flow")
        self.assertEqual(q.longest_common_prefix(["flow", "flower"]), "flow")
        self.assertEqual(q.longest_common_prefix(["flow", "flower", "float"]), "flo")
        self.assertEqual(q.longest_common_prefix(["cat", "dog", "frog"]), "")

    def test_count_letter_appearances(self):
        self.assertEqual(q.count_letter_appearances('word'), dict({'w': 1, 'o': 1, 'r': 1, 'd': 1}))
        self.assertEqual(q.count_letter_appearances('brontosaurus'),
                         dict({'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}))


if __name__ == '__main__':
    unittest.main()
