import csv_worker


class Algorithm:
    def __init__(self, csv_array):
        self.csv_array = csv_array
        
    def short_position(self, count_period=2):
        csv_array = self.csv_array
        min = count_period
        min_pos = 0

        for i in range(len(csv_array) - 1):
            if csv_array[i]["<CLOSE>"] > csv_array[i + 1]["<CLOSE>"] and min_pos == 0:
                min -= 1
            if csv_array[i]["<CLOSE>"] < csv_array[i + 1]["<CLOSE>"] and min_pos == 0:
                min = count_period

            if min == 0 and min_pos == 0:
                csv_array[i + 1]["<SHORT>"] = 1
                csv_array[i + 1]["<POSITION>"] = -1
                min_pos = 1

            if min_pos != 0 and csv_array[i]["<CLOSE>"] < csv_array[i + 1]["<CLOSE>"]:
                csv_array[i + 1]["<POSITION>"] = -1
                min_pos += 1
            if min_pos != 0 and csv_array[i]["<CLOSE>"] > csv_array[i + 1]["<CLOSE>"]:
                csv_array[i + 1]["<POSITION>"] = -1
                min_pos = 1
            if min_pos == count_period + 1:
                csv_array[i + 1]["<POSITION>"] = 0
                csv_array[i + 1]["<SHORT_EXIT>"] = 1
                min = count_period
                min_pos = 0

        return csv_array

    def long_position(self, count_period=2):
        csv_array = self.csv_array
        max = count_period
        max_pos = 0

        for i in range(len(csv_array) - 1):
            if csv_array[i]["<CLOSE>"] < csv_array[i + 1]["<CLOSE>"] and max_pos == 0:
                max -= 1
            if csv_array[i]["<CLOSE>"] > csv_array[i + 1]["<CLOSE>"] and max_pos == 0:
                max = count_period

            if max == 0 and max_pos == 0:
                csv_array[i + 1]["<LONG>"] = 1
                csv_array[i + 1]["<POSITION>"] = 1
                max_pos = 1

            if max_pos != 0 and csv_array[i]["<CLOSE>"] > csv_array[i + 1]["<CLOSE>"]:
                csv_array[i + 1]["<POSITION>"] = 1
                max_pos += 1

            if max_pos != 0 and csv_array[i]["<CLOSE>"] < csv_array[i + 1]["<CLOSE>"]:
                csv_array[i + 1]["<POSITION>"] = 1
                max_pos = 1

            if max_pos == count_period + 2:
                csv_array[i + 1]["<POSITION>"] = 0
                csv_array[i]["<LONG_EXIT>"] = 1
                max = count_period
                max_pos = 0

        return csv_array

    def fill_with_procents(self,count_period=2):
        csv_array = self.csv_array
        for i in range(count_period,len(csv_array)):
            csv_array[i]['<TODAY_INCOME>'] = round(
                (float(csv_array[i]['<CLOSE>']) - float(csv_array[i - 1]['<CLOSE>'])) * 100.0 / float(
                    csv_array[i - 1]['<CLOSE>']) * csv_array[i - 1]['<POSITION>'], 2)
            csv_array[i]['<TOTAL_INCOME>'] = round(csv_array[i - 1]['<TOTAL_INCOME>'] + csv_array[i]['<TODAY_INCOME>'], 2)

        return csv_array

    def fill_with_zeros(self):
        csv_array = self.csv_array
        for i in range(1,len(csv_array)):
            if(csv_array[i-1]['<POSITION>'] == -1 & csv_array[i]['<POSITION>'] == 1 ):
                csv_array[i]['<POSITION>'] = 0
        return csv_array

    # def long_position(self, count_period=2):
    #     csv_array = self.csv_array
    #     maximum = count_period
    #     max_pos = 0
    #     minimum = count_period
    #     min_pos = 0
    #
    #     for i in range(len(csv_array) - 1):
    #         if csv_array[i]["<CLOSE>"] < csv_array[i + 1]["<CLOSE>"] and max_pos == 0 and min_pos == 0:
    #             maximum -= 1
    #         if csv_array[i]["<CLOSE>"] > csv_array[i + 1]["<CLOSE>"] and max_pos == 0 and min_pos == 0:
    #             maximum = count_period
    #
    #         if csv_array[i]["<CLOSE>"] > csv_array[i + 1]["<CLOSE>"] and max_pos == 0 and min_pos == 0:
    #             minimum -= 1
    #         if csv_array[i]["<CLOSE>"] < csv_array[i + 1]["<CLOSE>"] and max_pos == 0 and min_pos == 0:
    #             minimum = count_period
    #
    #         if maximum == 0 and max_pos == 0:
    #             csv_array[i + 1]["<LONG>"] = 1
    #             csv_array[i + 1]["<POSITION>"] = 1
    #             max_pos = 1
    #
    #         if minimum == 0 and min_pos == 0:
    #             csv_array[i + 1]["<SHORT>"] = 1
    #             csv_array[i + 1]["<POSITION>"] = -1
    #             min_pos = 1
    #
    #         if max_pos != 0 and csv_array[i]["<CLOSE>"] > csv_array[i + 1]["<CLOSE>"]:
    #             csv_array[i + 1]["<POSITION>"] = 1
    #             max_pos += 1
    #         if max_pos != 0 and csv_array[i]["<CLOSE>"] < csv_array[i + 1]["<CLOSE>"]:
    #             csv_array[i + 1]["<POSITION>"] = 1
    #             max_pos = 1
    #
    #         if min_pos != 0 and csv_array[i]["<CLOSE>"] < csv_array[i + 1]["<CLOSE>"]:
    #             csv_array[i + 1]["<POSITION>"] = -1
    #             min_pos += 1
    #         if min_pos != 0 and csv_array[i]["<CLOSE>"] > csv_array[i + 1]["<CLOSE>"]:
    #             csv_array[i + 1]["<POSITION>"] = -1
    #             min_pos = 1
    #
    #         if min_pos == count_period + 1:
    #             csv_array[i + 1]["<POSITION>"] = 0
    #             min_pos = 0
    #
    #         if max_pos == count_period + 1:
    #             csv_array[i + 1]["<POSITION>"] = 0
    #             csv_array[i + 1]["<LONG_EXIT>"] = 1
    #             max_pos = 0
    #
    #     return csv_array


if __name__ == "__main__":
    csvArray = csv_worker.CsvReader('TATN_151029_201029.csv').csv_to_dict()
    csvArray = csv_worker.CsvDictEditor(csvArray).transformed_csv()
    csvAlgorithm = Algorithm(csvArray)
    csv = csvAlgorithm.short_position()
    csvAlgorithm = Algorithm(csv)
    csv = csvAlgorithm.long_position()
    csvAlgorithm = Algorithm(csv)
    csv = csvAlgorithm.fill_with_zeros()
    csvAlgorithm = Algorithm(csv)
    csv = csvAlgorithm.fill_with_procents()
    # csvAlgorithm = Algorithm(csv)
    # csv = csvAlgorithm.short_position()


    for row in csv:
        print(row)