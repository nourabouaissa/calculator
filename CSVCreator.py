import csv

class CSVCreator:
    def __init__(self, filename):
        self.filename = filename

    def create_csv(self, data):
        with open(self.filename, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            for number in data:
                csv_writer.writerow([number])
