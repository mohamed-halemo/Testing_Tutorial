
import time

class Performance_Mimick:
    def __init__(self, calculator):

        self.calculator = calculator

    def measure_time(self, operation, *args):
        """Measure execution time of a given operation"""
        start_time = time.time()
        result = operation(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time

    def test_operations(self, iterations=1000):
        """Test all basic calculator operations multiple times"""
        # Addition test
        add_results = []
        for _ in range(iterations):
            result, exec_time = self.measure_time(self.calculator.add, 5, 3)
            add_results.append(exec_time)

        # Subtraction test
        sub_results = []
        for _ in range(iterations):
            result, exec_time = self.measure_time(self.calculator.subtract, 5, 3)
            sub_results.append(exec_time)

        # Multiplication test
        mul_results = []
        for _ in range(iterations):
            result, exec_time = self.measure_time(self.calculator.multiply, 5, 3)
            mul_results.append(exec_time)

        # Division test
        div_results = []
        for _ in range(iterations):
            result, exec_time = self.measure_time(self.calculator.divide, 5, 2)  # Avoid division by zero
            div_results.append(exec_time)

        return {
            "addition": add_results,
            "subtraction": sub_results,
            "multiplication": mul_results,
            "division": div_results,
        }

    def print_performance(self, iterations=1000):
        results = self.test_operations(iterations)
        for operation, times in results.items():
            print(f"{operation.capitalize()} execution times:")
            print(f"Total time: {sum(times):.6f}s, Average time: {sum(times)/iterations:.6f}s")
            print(f"Max time: {max(times):.6f}s, Min time: {min(times):.6f}s\n")
