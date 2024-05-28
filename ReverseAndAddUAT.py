import unittest
import ReverseAndAdd

class TestReverseAndAdd(unittest.TestCase):
    def test_reverse_and_add(self):
        # Test case 1: Positive numbers
        self.assertEqual(ReverseAndAdd.reverseandAdd(123, 456), 579)

        # Test case 2: Negative Numbers
        self.assertEqual(ReverseAndAdd.reverseandAdd(-123, -456), -579)

        # Test case 3: Mixed positive and negative numbers
        self.assertEqual(ReverseAndAdd.reverseandAdd(123, -456), -333)

        # Test case 4: Zeroes - To ensure zero handled correctly
        self.assertEqual(ReverseAndAdd.reverseandAdd(0, 0), 0)

        # Test case 5: Zero and a number
        self.assertEqual(ReverseAndAdd.reverseandAdd(0, 1234), 4321)

        # Test case 6: Large numbers
        self.assertEqual(ReverseAndAdd.reverseandAdd(987654321, 123456789), 111111111)

        # Test case 7: Palindromic numbers
        self.assertEqual(ReverseAndAdd.reverseandAdd(121, 343), 464)

        # Test case 8: Both same numbers but in positive and negative resulting in zero
        self.assertEqual(ReverseAndAdd.reverseandAdd(-123, 123), 0)


if __name__ == '__main__':
    unittest.main()

