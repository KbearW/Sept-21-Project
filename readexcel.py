import pandas as pd

xls = pd.ExcelFile('samplefile.xlsx')
df1 = pd.read_excel(xls, 'Sheet1')
df2 = pd.read_excel(xls, 'Sheet2')

print(df1)
#print(df2)
#print(df1.iloc[0])
#print(df1[iloc[0]].values[0])
#print(df1.iloc[0]['A'])
df1['DataRange6'] = df1['DateRange1']+ df1['DateRange2']

#print first 5 rows of the data
print(df1)
writer = pd.ExcelWriter('new_book.xlsx')
df1.to_excel(writer, 'new_sheet')
writer.save()