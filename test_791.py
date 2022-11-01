import unittest
from solution_791 import Solution


class Test791(unittest.TestCase):

    def setUp(self):
        self.function = Solution()

    def test_1(self):
        resultado = self.function.customSortString("cba", "abcd")
        self.assertEqual(resultado, "cbad")

    def test_2(self):
        resultado = self.function.customSortString("rpo", "aofrpt")
        self.assertEqual(resultado, "rpoaft")


if __name__ == '__main__':
    unittest.main()
    
    