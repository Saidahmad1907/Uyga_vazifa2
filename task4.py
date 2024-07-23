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

class Converter(Calculate):
    @staticmethod
    def km_to_metr(km):
        return km * 1000
    
    @staticmethod
    def metr_to_sm(m):
        return m * 100
    
    @staticmethod
    def sm_to_mm(cm):
        return cm * 10


calculate = Calculate()

km = 5
metr = 3
cm = 2


km_to_metr_result = Converter.km_to_metr(km)
print(f"{km} km = {km_to_metr_result} metr")


metr_to_sm_result = Converter.metr_to_sm(metr)
print(f"{metr} metr = {metr_to_sm_result} santimetr")


sm_to_mm_result = Converter.sm_to_mm(cm)
print(f"{cm} santimetr = {sm_to_mm_result} millimetr")


summa_result = calculate.summa(10, 5)
print(f"Summa: {summa_result}")

difference_result = calculate.difference(10, 5)
print(f"Difference: {difference_result}")

multiple_result = calculate.multiple(10, 5)
print(f"Multiple: {multiple_result}")

division_result = calculate.division(10, 5)
print(f"Division: {division_result}")
