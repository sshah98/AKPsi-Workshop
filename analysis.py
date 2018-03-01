import pandas
import numpy
import xlrd
# import matplotlib.pyplot as plt

from openpyxl import load_workbook

# plt.style.use('ggplot')

myfile = "FinancialSample.xlsx"
path = r'/home/suraj/Desktop/akpsi-workshop/FinancialSample.xlsx'

def writeToSheet():
    writer = pd.ExcelWriter(path, engine='openpyxl')
    book = load_workbook(path)
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    data_df.to_excel(writer, sheet_name='Sheet2')
    writer.save()

def firstFunc():
    
    df = pandas.read_excel(myfile, 'Sheet1')

    data_df = df.iloc[:,0:2]
        
    df['Sum'] = df['Units Sold']
    print(df['Sum'].mean())
    # print(df.head())
    # print(data_df)


firstFunc()




