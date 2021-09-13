import pandas as pd
import numpy as np

xls = pd.ExcelFile('Testing file 9.7.xlsx')
# df1 = pd.read_excel(xls, 'REGN Pral Clinical Studies', skiprows = [0])
df1 = pd.read_excel(xls, 'REGN Pral Clinical Studies')

# df2 = pd.read_excel(xls, 'REGN Pral FTEs')

# print('file found')
# print(df1.head())

# print(columns)
# print(df2.head())
# Carryfwd value from prior (forward fill = ffill)
rows, columns = df1.shape 
# columns = df1.columns.tolist()
# print(columns[0:3])
# rows = df1.rows.tolist()
print(rows, columns)
print(f'rows: {rows}')
print(f'cols: {df1.iloc[1:5]}')
print('%%'*60)
print(f'a specific location (R,C) (2,10) should be 606:{df1.iloc[2,10]}')

print(f'a specific location (R,C) (0,0) should be BudgetType:{df1.iloc[0,0]}')
print(f'a specific location (R,C) (1,0) should be Development:{df1.iloc[1,0]}')
print(f'a specific location (R,C) (0,1) should be Activity:{df1.iloc[0,1]}')
print(f'a specific location (R,C) (0,3) should be clinical study name:{df1.iloc[0,3]}')


print('******'*20)

''' Data forwardfill '''
# info = [columns[x] for str(x) in range(0,4)]
# df1[info] = df1[info].fillna(method='ffill')

def assign_quarterly_sum(array_name, quarter_name, row_number, column_number, sheet):
    '''recalculate total based on clinical study number'''
    array_name[quarter_name] = 0
    if 'Total' in str(df1.iloc[row,0]) or 'Total' in str(df1.iloc[row,1]) or 'Total' in str(df1.iloc[row,2]):
        pass
    array_name[quarter_name] += df1.iloc[row, column_number]

header = True
for row in range(rows):
    if header:
        if df1.iloc[row,0] =='Budget Type': 
            header = False
            # print(row, 'label row- skip')
    else:
        budget = {}
        reforecast = {}
        actual = {}

        assign_quarterly_sum( budget, 'Q1', row, 5, df1)
        assign_quarterly_sum( budget, 'Q2', row, 6, df1)
        assign_quarterly_sum( budget, 'Q3', row, 7, df1)
        assign_quarterly_sum( budget, 'Q4', row, 8, df1)
        assign_quarterly_sum( budget, 'FY', row, 9, df1)

        assign_quarterly_sum( reforecast, 'Q1', row, 10, df1)
        assign_quarterly_sum( reforecast, 'Q2', row, 11, df1)
        assign_quarterly_sum( reforecast, 'Q3', row, 12, df1)
        assign_quarterly_sum( reforecast, 'Q4', row, 13, df1)
        assign_quarterly_sum( reforecast, 'FY', row, 14, df1)
        
        assign_quarterly_sum( actual, 'Q1', row, 15, df1)
        assign_quarterly_sum( actual, 'Q2', row, 16, df1)
        assign_quarterly_sum( actual, 'Q3', row, 17, df1)
        assign_quarterly_sum( actual, 'Q4', row, 18, df1)
        assign_quarterly_sum( actual, 'FY', row, 19, df1)
        
# res = {}
# res['reforecast'] = reforecast
print(budget)
print(reforecast)
print(actual)
# print(res)

# df1['testing- blank'] = "123545"

# df1['recal'] = budget

# # # Fill NA with zeros
# # numeric_data = [columns[x] for x in range(5,31)]
# # print(numeric_data)
# # df1[numeric_data] = df1[numeric_data].fillna(0)
# # print(df1.loc['54321'])
# print('-----'*30)
# print(df1[1:3])

# print(f"rows: {rows}")
# print(f"columns: {columns}")

# # # Fill NA with zeros
# # numeric_data = [columns[x] for x in range(5,20)]
# # print(numeric_data)
# # # df1[numeric_data] = df1[numeric_data].fillna(0)

# # print(type(df1[columns[2]]))
# # print(df1[columns[2].astype(basestring)])

# # df1.append(df1[[columns[5]]].sum().rename('Grandtotal33')).fillna('')

# # '''--->'''
# # df1.loc['GrandTotal'] = df1[[columns[x] for x in range(5,20)]].sum()
# # # df1.loc['GrandTotal55'] = df1.loc['GrandTotal55'].fillna('')

writer = pd.ExcelWriter('new_book.xlsx')
df1.to_excel(writer, 'new_sheet')
writer.save() 