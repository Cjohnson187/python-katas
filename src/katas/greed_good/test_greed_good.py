from unittest import TestCase

from numpy.ma.testutils import assert_equal

from src.katas.greed_good.greed_good import score


class Test(TestCase):
    def test_score(self):
        assert_equal(score([5, 1, 3, 4, 1]), 250)
        assert_equal(score([1, 1, 1, 3, 1]), 1100)
        assert_equal(score([2, 3, 4, 6, 2]), 0)
        assert_equal(score([4, 4, 4, 3, 3]), 400)
        assert_equal(score([2, 4, 4, 5, 4]), 450)
    def test_score_1(self):
        assert_equal(score([1, 1, 1, 1, 1]), 1200)
    def test_score_2(self):
        assert_equal(score([1, 1, 1, 3, 1]), 1100)

