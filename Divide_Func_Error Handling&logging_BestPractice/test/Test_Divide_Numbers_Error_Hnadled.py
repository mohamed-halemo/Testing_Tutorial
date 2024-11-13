from app.Divide_Num_Error_Handled import divide_numbers
import unittest

class TestDivideNumbers(unittest.TestCase):

    def test_divide_valid_numbers(self):
        # Arrange: Prepare input values
        a = 10
        b = 2
        expected_result = 5

        # Act: Perform the division
        result = divide_numbers(a, b)

        # Assert: Check if the result is as expected
        self.assertEqual(result, expected_result)

    def test_divide_by_zero(self):
        # Arrange: Prepare input values
        a = 10
        b = 0

        # Act: Perform the division, expecting a ValueError to be raised
        with self.assertRaises(ValueError) as context:
            divide_numbers(a, b)

        # Assert: Check if the exception message matches
        self.assertEqual(str(context.exception), "Cannot divide by zero.")

if __name__ == '__main__':
    unittest.main()
