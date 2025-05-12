import unittest
from binary_search_704 import Solution

class TestSolution(unittest.TestCase):

    def test_search_1(self):
        sol = Solution()
        result = sol.search([-1, 0, 3, 5, 9, 12], 9)
        self.assertEqual(result, 4)  # Expected output: 4

    def test_search_2(self):
        sol = Solution()
        result = sol.search([-1, 0, 3, 5, 9, 12], 2)
        self.assertEqual(result, -1)  # Expected output: -1

    def test_search_empty(self):
        sol = Solution()
        result = sol.search([], 5)
        self.assertEqual(result, -1)  # Edge case: Empty array, expected output: -1

    def test_search_not_found(self):
        sol = Solution()
        result = sol.search([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, -1)  # Expected output: -1, since 6 is not in the array

    def test_search_first_element(self):
        sol = Solution()
        result = sol.search([1, 2, 3, 4, 5], 1)
        self.assertEqual(result, 0)  # Expected output: 0, since 1 is at index 0

