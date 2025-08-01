def calculator_function(a, b, operation):
    
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    elif operation == 'power':
        return a ** b
    elif operation == 'modulus':
        if b == 0:
            raise ValueError("Cannot perform modulus by zero.")
        return a % b
    else:
        raise ValueError("Invalid operation. Choose from 'add', 'subtract', 'multiply', 'divide', 'power', 'modulus'.")
    
calculator_function(10, 5, 'add')