from unittest import TestCase
from numpy.ma.testutils import assert_equal
from src.katas.number_sums.number_sum_combos import combos


class Test(TestCase):

    def do_test(self,  n: int, expected: list[list[int]]):
        actual = combos(n)
        if not isinstance(actual, list) or not all(isinstance(x, list) for x in actual):
            assert False, f'for n = {n}, expected a list of lists, but got {repr(actual)}'
        actual = sorted(map(sorted, actual))
        expected = sorted(map(sorted, expected))
        assert_equal(actual, expected, f'for n = {n}, after sorting:\n \n')

    def test_combos(self):
        self.do_test(1, [[1]])
        self.do_test(2, [[1, 1], [2]])
        self.do_test(3, [[1, 1, 1], [1, 2], [3]])
        self.do_test(4, [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2], [4]])

    def test_combo_1(self):
        self.do_test(1, [[1]])

    def test_combo_2(self):
        self.do_test(2, [[1, 1], [2]])

    def test_combo_3(self):
        self.do_test(3, [[1, 1, 1], [1, 2], [3]])