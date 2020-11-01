import csv


class CsvReader:
    def __init__(self, path):
        self.path = path

    def csv_to_dict(self):
        row_array = list()
        with open(self.path) as f:
            records = csv.DictReader(f)
            for row in records:
                row_array.append(row)
        return row_array


class CsvDictEditor:
    def __init__(self, csv_array):
        self.csv_array = csv_array

    def __del_extra_field(self):
        csv_array = self.csv_array
        for i in range(len(csv_array)):
            del csv_array[i]["<PER>"]
            del csv_array[i]["<TIME>"]
            del csv_array[i]["<OPEN>"]
            del csv_array[i]["<HIGH>"]
            del csv_array[i]["<LOW>"]
            del csv_array[i]["<VOL>"]
        return csv_array

    def __add_extra_field(self):
        csv_array = self.__del_extra_field()
        for i in range(len(csv_array)):
            csv_array[i]["<SHORT>"] = 0
            csv_array[i]["<LONG>"] = 0
            csv_array[i]["<SHORT_EXIT>"] = 0
            csv_array[i]["<LONG_EXIT>"] = 0
            csv_array[i]["<POSITION>"] = 0
            csv_array[i]["<TODAY_INCOME>"] = 0
            csv_array[i]["<TOTAL_INCOME>"] = 0
        return csv_array

    def transformed_csv(self):
        return self.__add_extra_field()


if __name__ == "__main__":
    csvArray = CsvReader('TATN_151029_201029.csv').csv_to_dict()
    csvArray = CsvDictEditor(csvArray).transformed_csv()
    for row in csvArray:
        print(row)
