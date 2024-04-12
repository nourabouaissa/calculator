from CSVCreator import CSVCreator
from CSVReader import CSVReader
from Calculator import Calculator
from ResultPrinter import ResultPrinter

if __name__ == "__main__":
    filename = 'numbers.csv'
    data = [1, 2, 3]
   #data
    csv_creator = CSVCreator(filename)
    csv_creator.create_csv(data)
    csv_reader = CSVReader(filename)
    numbers = csv_reader.read_data()

    calculator = Calculator()
    total_add, results_add = calculator.calculate_addition(numbers)
    total_mul, results_mul = calculator.calculate_multiplication(numbers)
    #display
    ResultPrinter.print_results(total_add, results_add, 'addition')
    ResultPrinter.print_results(total_mul, results_mul, 'multiplication')
