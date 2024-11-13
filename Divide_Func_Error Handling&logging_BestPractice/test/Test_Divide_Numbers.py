from app.Divide_num import divide_numbers

import unittest

class TestDivideNumbers(unittest.TestCase):

    def test_divide_valid_numbers(self):
        
        # Arrange: Prepare input values
        a=10
        b=5
        expected_results=2
        # Act: Perform the division
        result=divide_numbers(a,b)
        # Assert: Check if the result is as expected
        self.assertEqual(result,expected_results)

    def test_divide_by_zero(self):
        pass
        
        # Arrange: Prepare input values for division by zero
        a=10
        b=0

        # # Act & Assert: Check if the ZeroDivisionError is raised
        
        #it will fail modified code under error handled name to see the solution
        with self.assertRaises(ValueError):
            divide_numbers(a,b)

if __name__ == '__main__':
    unittest.main()
