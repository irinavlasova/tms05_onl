import unittest
from tests.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        print("finish")

    def test_sum_pos(self):
        answer = self.calc.sum(5, 4)
        self.assertEqual(answer, 9)

    def test_sum_neg(self):
        answer = self.calc.sum(5, 4)
        self.assertNotEqual(answer, 9)

    def test_sub_pos(self):
        answer = self.calc.sub(5, 4)
        self.assertEqual(answer, 1)

    def test_sub_neg(self):
        answer = self.calc.sub(5, 4)
        self.assertNotEqual(answer, 1)

    def test_mul_pos(self):
        answer = self.calc.mul(5, 4)
        self.assertEqual(answer, 20)

    def test_mul_neg(self):
        answer = self.calc.mul(5, 4)
        self.assertIsNot(answer, 20)

    def test_div_ops(self):
        answer = self.calc.div(5, 5)
        self.assertEqual(answer, 1)

    def test_div_neg(self):
        answer = self.calc.div(5, 5)
        self.assertNotEqual(answer, 1)


if __name__ == "__main__":
    unittest.main()
