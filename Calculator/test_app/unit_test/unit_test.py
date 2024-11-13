from app.Calculator_Class import Calculator
import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Arrange: Initialize the Calculator instance
        self.calculator = Calculator()

    def test_add(self):
        # Arrange: Prepare input values
        a=10
        b=5
        expected_result=15
       
        # Act: Perform the addition
        result=self.calculator.add(a,b)
        # Assert: Check if the result is as expected
        self.assertEqual(result,expected_result)

    def test_subtract(self):
        
        # Arrange: Prepare input values
        a=10
        b=5
        expected_results=5

        # Act: Perform the subtraction
        result=self.calculator.subtract(a,b)
        # Assert: Check if the result is as expected
        self.assertEqual(result,expected_results)

    def test_multiply(self):
        
        # Arrange: Prepare input values
        a=10
        b=5
        expected_result=50

        # Act: Perform the multiplication
        result=self.calculator.multiply(a,b)
    
        # Assert: Check if the result is as expected


    def test_divide(self):
        
        # Arrange: Prepare input values
        a=10
        b=5
        expected_result=2
    

        # Act: Perform the division
        result=self.calculator.divide(a,b)
        # Assert: Check if the result is as expected
        self.assertEqual(result,expected_result)

    def test_divide_by_zero(self):
        a=10
        b=0
        # Arrange: Prepare input values for division by zero
     

        # Act & Assert: Check if the ValueError is raised for division by zero
        with self.assertRaises(ValueError):
            self.calculator.divide(a,b)

if __name__ == '__main__':
    unittest.main()
