import pandas as pd

xls = pd.ExcelFile('Total Program Alirocumab (REGN727) - Day 30_Final v2.xlsx')
df1 = pd.read_excel(xls, 'REGN Pral Clinical Studies', skiprows = [0])

# df2 = pd.read_excel(xls, 'REGN Pral FTEs')

# print('file found')
# print(df1.head())

# print(columns)
# print(df2.head())
# Carryfwd value from prior (forward fill = ffill)
columns = df1.columns.tolist()
print(columns[0:3])

# This inplace method doesn't work but the next line does- why?
df1[[columns[0]]].fillna(method='ffill', inplace = True)
# df1[[columns[0], columns[1], columns[2], columns[3]]] = df1[[columns[0], columns[1], columns[2], columns[3]]].fillna(method='ffill')
# df1[[['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3']]] = df1[['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3']].fillna(method='ffill')
print(df1.head())


# writer = pd.ExcelWriter('new_book.xlsx')
# df1.to_excel(writer, 'new_sheet')
# writer.save() 