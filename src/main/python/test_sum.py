from unittest import TestCase
from sum import sum


class Test(TestCase):
    def test_sum_ok(self):
        self.assertEqual(sum(5,7), 12)

    def test_sum_float(self):
        self.assertEqual(sum(5.3, 7.8), 13.1, 7)


if __name__ == "__main__":
    unittest.main()
