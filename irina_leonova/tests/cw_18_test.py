import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("I am setup method.")

    def tearDown(self):
        print("I am teardown method.")

    def test_sum(self):
        a = 3 + 5
        self.assertEqual(a, 8)

    @unittest.skip("Меня пофиксят")
    def test_sub(self):
        a = 5 - 3
        self.assertIs(a, 2)


if __name__ == "__main__":
    unittest.main()
