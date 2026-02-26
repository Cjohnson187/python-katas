from unittest import TestCase
from numpy.ma.testutils import assert_equal

from src.katas.coutning_duplicates.coutning_duplicates import duplicate_count

class TestCountingDuplicates(TestCase):
    def test_duplicate_count(self):
        assert_equal(duplicate_count(""), 0, 'duplicate_count("")')
        assert_equal(duplicate_count("abcde"), 0, 'duplicate_count("abcde")')
        assert_equal(duplicate_count("abcdeaa"), 1, 'duplicate_count("abcdeaa")')
        assert_equal(duplicate_count("abcdeaB"), 2, 'duplicate_count("abcdeaB")')

        assert_equal(duplicate_count("Indivisibilities"), 2, 'duplicate_count("Indivisibilities")')

