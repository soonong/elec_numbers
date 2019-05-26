import openpyxl as openpyxl
import json
import pandas as pd


# def elec_info_save(filename):
#     data = filename
#     dataframe = pd.DataFrame(data)
#     dataframe.to_csv('{}.csv'.format(filename), encoding='ms949', header=False, index=False)


def elec_info_save(filename):
    data = filename
    dataframe = pd.DataFrame(data)
    dataframe.to_csv('1-2000.csv', encoding='ms949', header=False, index=False)

