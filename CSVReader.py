import csv

class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        data = []
        with open(self.filename, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(int(row[0]))
        return data
