class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        raise ValueError("Cannot divide by zero")
    @staticmethod
    def subtract(a, b):
        return a - b

Calculator.add(2, 3)
print(Calculator.add(2, 3))
Calculator.multiply(2, 3)
print(Calculator.multiply(2, 3))
Calculator.divide(2, 1)
print(Calculator.divide(2, 1))
Calculator.subtract(2, 3)
print(Calculator.subtract(2, 3))

