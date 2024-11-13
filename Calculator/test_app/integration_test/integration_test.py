from app.Calculator_Class import Calculator
import unittest

class TestCalculatorIntegration(unittest.TestCase):

    def setUp(self):
        # Arrange: Initialize the Calculator instance
        self.calculator = Calculator()

    def test_operations_sequence(self):
        
        # Arrange: Prepare input values
        a=10
        b=5
        c=2
        expected_results= 5      #((10+5)-5)/2=5

        # Act: Perform the operations
        result=self.calculator.add(a,b)  #10+5=15
        result=self.calculator.subtract(result,b) #15-5=10
        result=self.calculator.divide(result,c)  #10/2=5

        # Assert: Check if the final result is as expected
        self.assertEqual(result,expected_results)

if __name__ == '__main__':
    unittest.main()
