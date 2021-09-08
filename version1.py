import pandas as pd
import numpy as np

xls = pd.ExcelFile('Testing file 9.7.xlsx')
df1 = pd.read_excel(xls, 'REGN Pral Clinical Studies', skiprows = [0])

# df2 = pd.read_excel(xls, 'REGN Pral FTEs')

# print('file found')
# print(df1.head())

# print(columns)
# print(df2.head())
# Carryfwd value from prior (forward fill = ffill)
columns = df1.columns.tolist()
print(columns[0:3])

# issues:
# 1.) it takes a few secs to run the file, is it normal?
# This inplace method doesn't work but the next line does- why?
# df1[[columns[0]]].fillna(method='ffill', inplace = True)

# Data backfills
# Fill NA with information (fwdfill)
info = [columns[x] for x in range(0,4)]
df1[info] = df1[info].fillna(method='ffill')

# Fill NA with zeros
numeric_data = [columns[x] for x in range(5,20)]
print(numeric_data)
# df1[numeric_data] = df1[numeric_data].fillna(0)

df1[[columns[2]]] = df1[[columns[2].str.contains('Total')==False]]
print(type(df1[columns[2]]))
# print(df1[columns[2].astype(basestring)])

# Can use lambda function here...
df1[''] = ""
df1['Budget FY recal'] = df1[columns[5]] + df1[columns[6]] + df1[columns[7]] + df1[columns[8]] - df1[columns[9]]
df1['April Reforecast FY recal'] = df1[columns[10]] + df1[columns[11]] + df1[columns[12]] + df1[columns[13]] - df1[columns[14]]
df1['Actuals FY recal'] = df1[columns[15]] + df1[columns[16]] + df1[columns[17]] + df1[columns[18]] - df1[columns[19]]
df1['April Reforecast FY recal'] = df1[columns[10]] + df1[columns[11]] + df1[columns[12]] + df1[columns[13]] - df1[columns[14]]
# print(df1.head())

df1.append(df1[[columns[5]]].sum().rename('Grandtotal33')).fillna('')

'''--->'''
df1.loc['GrandTotal'] = df1[[columns[x] for x in range(5,20)]].sum()
# df1.loc['GrandTotal55'] = df1.loc['GrandTotal55'].fillna('')

# for label, _df in df1.groupby(columns[5],columns[6]):
#     print(label)
#     print(_df)
#     print()

writer = pd.ExcelWriter('new_book.xlsx')
df1.to_excel(writer, 'new_sheet')
writer.save() 