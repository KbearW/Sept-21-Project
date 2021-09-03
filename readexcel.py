import pandas as pd

xls = pd.ExcelFile('samplefile.xlsx')
df1 = pd.read_excel(xls, 'Sheet1')
#df2 = pd.read_excel(xls, 'Sheet2')

# print(df1)

print(f'column names: {df1.columns[0]}')

# print(df1['Unnamed: 0'])
# print(df1['Unnamed: 5'])
# print(df1['DateRange1'])
# print(df1['DateRange2'])
# print(df1['DateRange3'])
# print(df1['DateRange4'])

# should return the rows: [item1, item2, item3, item4]
# print(df1.head().index.tolist())
# print('*'*20)
# print(df1.iloc[0:4])

# # get '333' --> iloc[R,C]
# print(f'This should return 333: {df1.iloc[2,3]}')


# # how to drop the leading 
# print(f"Items: {df1['Unnamed: 0']}")

# print(df1.loc[1:3, :])

# print(df1.loc[1:3, 'DateRange3':'DateRange4'])

# print(df1.loc[df1['Unnamed: 0']=='Item3',:])

# # This is powerful and what you need to get a specific cell! 
# print(f"This is a filter function returning item3s datarange4: {df1.loc[df1['Unnamed: 0']=='Item3','DateRange4']}")

# # loc is for labels --> inclusive [0:3] --> (0,1,2,3)
# # iloc is for indexing--> exclusive [0:3] --> (0,1,2)

# # Uses indexing 
# print(df1.iloc[:,1:3])


# # for row in df1.index():
# #     print(row)

# # print('L18')
# # # get the ith col
# # print(df1.iloc[0])

# # # print('L22')
# # # #get the ith row
# # print(df1.iloc[[1]])

# #print(df1.loc[df1['DateRange2']==2])
# #print('*'*20)
# #for col in df1.columns:
# #    print(col)

# #print(df1.columns.values.tolist())




# #print(df1['DataRange2'])
# #print(df1.columns.get_loc('DataRange2'))
# #print(df1['DataRange2','DataRange4'])

# #print(df1.rows)
# #print(df2)
# #print(df1.iloc[0])
# #print(df1[iloc[0]].values[0])
# #print(df1.iloc[0]['A'])
# df1['DataRange6'] = df1['DateRange1']+ df1['DateRange2']

# #print first 5 rows of the data
# #print(df1)
# #writer = pd.ExcelWriter('new_book.xlsx')
# #df1.to_excel(writer, 'new_sheet')
# #writer.save()