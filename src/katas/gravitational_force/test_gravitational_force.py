from unittest import TestCase

from numpy.ma.testutils import assert_equal

from src.katas.gravitational_force.gravitational_force import solution


class TestGravitationalForce(TestCase):
    def setUp(self):
        self.valid_arr_val = [1000, 1000, 100]
        self.valid_arr_unit = ["g", "kg", "m"]
        self.invalid_valid_arr_val = []
        self.invalid_valid_arr_unit = []

    def test_solution_1(self):
        assert_equal(solution([1000, 1000, 100], ["g", "kg", "m"]), 6.67e-12)

    def test_solution_2(self):
        assert_equal(solution([1000, 1000, 100], ["kg", "kg", "m"]), 6.667e-9)

    def test_solution_3(self):
        assert_equal(solution([1000, 1000, 100], ["kg", "kg", "cm"]), 0.0000667)

    def test_solution_4(self):
        assert_equal(solution([100001.0, 200001.0, 0.3], ["lb", "μg", "μm"]), 6723.355751239066)

    def test_solution_5(self):
        assert_equal(solution([200001.0, 100001.0, 0.3], ['lb', 'g', 'ft']), 0.07236945390785615)


    def test_solution_6(self):
        assert_equal(solution([100001.0, 200001.0, 0.3], ['lb', 'μg', 'μm']), 6723.342271179719)

# arr_val = [200001.0, 100001.0, 0.3]
# arr_unit = ['lb', 'g', 'ft']
#
# 0.07236959900600738 should be close to 0.07236945390785615 with absolute or relative margin of 1e-09


# arr_val = [100001.0, 200001.0, 0.3]
# arr_unit = ['lb', 'μg', 'μm']
#
# 6723.355751239066 should be close to 6723.342271179719 with absolute or relative margin of 1e-09