import logging
logging.basicConfig(filename='app.log', 
                    level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error("Division error: %s", e)
        raise ValueError("Cannot divide by zero.")
    



