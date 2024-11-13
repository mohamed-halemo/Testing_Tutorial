import logging

# Configure logging
logging.basicConfig(filename='calculator.log', 
                    level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            logging.error("Division error: %s", e)
            raise ValueError(e)
    

from app.Performance_Mimicking import Performance_Mimick

#intialize calcualtor & preformance test

calculator=Calculator()
Performance=Performance_Mimick(calculator)

Performance.print_performance(iterations=1000)