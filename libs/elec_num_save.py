import openpyxl as openpyxl
import json
import pandas as pd



def elec_num_save(filename):
    data = filename
    dataframe = pd.DataFrame(data)
    dataframe.to_csv('elec_numbers.csv', encoding='ms949', header=False, index=False)


# import csv

# def save(filename):
#     data = filename
#     csvfile = open('ddddd.csv', 'w', newline="")
#     csvwriter = csv.writer(csvfile)
#     for row in data:
#         csvwriter.writerow(row)
#     csvfile.close()
#



# 타임스템프 로 저장?

