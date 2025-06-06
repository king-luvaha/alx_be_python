def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1: First number (float)
        num2: Second number (float)
        operation: Type of operation (add, subtract, multiply, divide)
        
    Returns:
        Result of the arithmetic operation as float.
        Returns "Error: Division by zero!" if attempting to divide by zero.
    """
    operation = operation.lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        return "Error: Invalid operation!"