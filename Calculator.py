
class Calculator:
    def __init__(self):
        self.total_add = 0
        self.total_mul = 1
        self.results_add = []
        self.results_mul = []

    def calculate_addition(self, data):
        for number in data:
            self.total_add += number
            self.results_add.append(f"+{number} (={self.total_add})")
        return self.total_add, self.results_add

    def calculate_multiplication(self, data):
        for number in data:
            self.total_mul *= number
            self.results_mul.append(f"*{number} (={self.total_mul})")
        return self.total_mul, self.results_mul
