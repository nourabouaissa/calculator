class ResultPrinter:
    @staticmethod
    def print_results(total, results, operation):
        print(f"{operation.capitalize()}:")
        for result in results:
            print(result)
        print("-------")
        print(f"total = {total} ({operation})")
