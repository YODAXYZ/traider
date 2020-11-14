from csv import DictWriter
import xlsxwriter
import os.path


def create_xlsx_file(file_path: str, headers: dict, items: list):
    with xlsxwriter.Workbook(file_path) as workbook:
        worksheet = workbook.add_worksheet()
        worksheet.write_row(row=0, col=0, data=headers.values())
        header_keys = list(headers.keys())
        for index, item in enumerate(items):
            row = map(lambda field_id: item.get(field_id, ''), header_keys)
            worksheet.write_row(row=index + 1, col=0, data=row)


class CsvWriter:

    def __init__(self, csv_array):
        self.csv_array = csv_array

    def writeToCsv(self):
        with open('results.csv', 'w') as outfile:
            writer = DictWriter(outfile, ('<TICKER>', '<DATE>', '<CLOSE>',
                                          '<SHORT>', '<LONG>', '<SHORT_EXIT>',
                                          '<LONG_EXIT>', '<POSITION>', '<TODAY_INCOME>', '<TOTAL_INCOME>'))
            writer.writeheader()
            writer.writerows(self.csv_array)

    def writeToXls(self, filename, csv):
        headers = {
            '<TICKER>': 'TICKER',
            '<DATE>': 'DATE',
            '<CLOSE>': 'CLOSE',
            '<SHORT>': 'SHORT',
            '<LONG>': 'LONG',
            '<SHORT_EXIT>': 'SHORT_EXIT',
            '<LONG_EXIT>': 'LONG_EXIT',
            '<POSITION>': 'POSITION',
            '<TODAY_INCOME>': 'TODAY_INCOME',
            '<TOTAL_INCOME>': 'TOTAL_INCOME'
        }
        if os.path.isfile(filename):
            print("File already exists!")
        else:
            create_xlsx_file(filename, headers, csv)

