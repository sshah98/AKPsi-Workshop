import pandas as pd
import numpy as np
from openpyxl import load_workbook
import xlrd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

myfile = "FinancialSample.xlsx"


path = r'/home/suraj/Desktop/akpsi-workshop/FinancialSample.xlsx'

print("Reading Data...")

df = pd.read_excel(myfile, 'Sheet1')
# print(df.head())

# plt.figure()

# print(df.mean())

data_df = df.iloc[:,0:2]


# df['Units Sold'][1:100].plot()
# plt.show()

# plt.show()
# print(df.)

# print(df.cumsum().plot())


# in all functions - writes to a new sheet using the dataframe created in function
writer = pd.ExcelWriter(path, engine='openpyxl')
book = load_workbook(path)
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
data_df.to_excel(writer, sheet_name='Sheet2')
writer.save()
