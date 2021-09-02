import pandas as pd

xls = pd.ExcelFile('samplefile.xlsx')
df1 = pd.read_excel(xls, 'Sheet1')
df2 = pd.read_excel(xls, 'Sheet2')
print(df1)
print(df2)
