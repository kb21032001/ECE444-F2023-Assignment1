import unittest
from Utils import Utils  # Import the Utils class from the utils.py file

class UtilsTest(unittest.TestCase):
    def test_reversed_int(self):
        self.assertEqual(Utils.reversed(12345), 54321)
        self.assertEqual(Utils.reversed(-6789), -9876)

    def test_reversed_string(self):
        with self.assertRaises(ValueError):
            Utils.reversed("12345")
        with self.assertRaises(ValueError):
            Utils.reversed("-6789")

    def test_reversed_float(self):
        with self.assertRaises(ValueError):
            Utils.reversed(123.45)
        with self.assertRaises(ValueError):
            Utils.reversed(-67.89)

    def test_formatter_int(self):
        binary, octal = Utils.formatter(42)
        self.assertEqual(binary, '0b101010')
        self.assertEqual(octal, '0o52')

    def test_formatter_string(self):
        with self.assertRaises(ValueError):
            Utils.formatter("42")

    def test_formatter_float(self):
        with self.assertRaises(ValueError):
            Utils.formatter(42.5)

if __name__ == "__main__":
    unittest.main()
