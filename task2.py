class Calculate:
    @staticmethod
    def summa(a, b):
        return a + b
    
    @staticmethod
    def difference(a, b):
        return a - b
    
    @staticmethod
    def multiple(a, b):
        return a * b
    
    @staticmethod
    def division(a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed"

print("Summa: ", Calculate.summa(10, 5))
print("Difference: ", Calculate.difference(10, 5))
print("Multiple: ", Calculate.multiple(10, 5))
print("Division: ", Calculate.division(10, 5))
print("Division by zero: ", Calculate.division(10, 0))
