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


print('******'*60)
# print(df1.iloc[3,2])  #'54321 Total'
# print('Total' in df1.iloc[3,2])  #True

reforecastQ1 = 0
reforecastQ2 = 0
reforecastQ3 = 0
reforecastQ4 = 0
reforecastFY = 0

reforecast = {}

header = True
for row in range(rows):
    if header:
        if df1.iloc[row,0] =='Budget Type': 
            header = False
            print('label row- skip')
    else:
        # print(df1.iloc[row,10])
        print(row)
        if 'Total' not in str(df1.iloc[row,0]) and 'Total' not in str(df1.iloc[row,1]) and 'Total' not in str(df1.iloc[row,2]):
            reforecastQ1 += df1.iloc[row,10]
            reforecastQ2 += df1.iloc[row,11]
            reforecastQ3 += df1.iloc[row,12]
            reforecastQ4 += df1.iloc[row,13]
            reforecastFY += df1.iloc[row,14]
reforecast['reforecastQ1'] = reforecastQ1
reforecast['reforecastQ2'] = reforecastQ2
reforecast['reforecastQ3'] = reforecastQ3
reforecast['reforecastQ4'] = reforecastQ4
reforecast['reforecastFY'] = reforecastFY

print(reforecast)


# reforecast = {}

# header = True
# for row in range(rows):
#     if header:
#         if df1.iloc[row,0] =='Budget Type': 
#             header = False
#             print('label row- skip')
#     else:
#         # print(df1.iloc[row,10])
#         print(row)
#         if 'Total' not in str(df1.iloc[row,0]) and 'Total' not in str(df1.iloc[row,1]) and 'Total' not in str(df1.iloc[row,2]):
#             reforecast.get('reforecastQ1',0) += df1.iloc[row,10]
#             reforecast.get('reforecastQ2',0) += df1.iloc[row,11]
#             reforecast.get('reforecastQ3',0) += df1.iloc[row,12]
#             reforecast.get('reforecastQ4',0) += df1.iloc[row,13]
#             reforecast.get('reforecastFY',0) += df1.iloc[row,14]


# print(reforecast)

# print(reforecast)

# print('+++++'*66)
# print(df1.columns)
# print(df1[['Activity ','Cost Type',  'April Reforecast Q1 2021']])

# print(rows)
# print('only return linew with total in activity, answer should be 1417.598705' )

# print(df1[['Activity ','Cost Type',  'April Reforecast Q1 2021']][df1['Activity ']=='Clinical Total'])
# df1.set_index('Clinical Study Number',inplace=True)
# print(df1.head())

# # print(type(columns))
# # print(type(rows))
# # print(df1[1:3])

# # # Fill NA with zeros
# # numeric_data = [columns[x] for x in range(5,31)]
# # print(numeric_data)
# # df1[numeric_data] = df1[numeric_data].fillna(0)
# # print(df1.loc['54321'])
# print('-----'*30)
# print(df1[1:3])

# print(f"rows: {rows}")
# print(f"columns: {columns}")

# # issues:
# # 1.) it takes a few secs to run the file, is it normal?
# # This inplace method doesn't work but the next line does- why?
# # df1[[columns[0]]].fillna(method='ffill', inplace = True)

# # Data backfills
# # Fill NA with information (fwdfill)
# # info = [columns[x] for x in range(0,4)]
# # df1[info] = df1[info].fillna(method='ffill')

# # # Fill NA with zeros
# # numeric_data = [columns[x] for x in range(5,20)]
# # print(numeric_data)
# # # df1[numeric_data] = df1[numeric_data].fillna(0)

# # print(type(df1[columns[2]]))
# # print(df1[columns[2].astype(basestring)])

# # Can use lambda function here...
# # df1[''] = ""

# # res = {}
# # res['Budget FY recal'] = df1[columns[5]] + df1[columns[6]] + df1[columns[7]] + df1[columns[8]] - df1[columns[9]]
# # res['April Reforecast FY recal'] = df1[columns[10]] + df1[columns[11]] + df1[columns[12]] + df1[columns[13]] - df1[columns[14]]
# # res['Actuals FY recal'] = df1[columns[15]] + df1[columns[16]] + df1[columns[17]] + df1[columns[18]] - df1[columns[19]]
# # res['April Reforecast FY recal'] = df1[columns[10]] + df1[columns[11]] + df1[columns[12]] + df1[columns[13]] - df1[columns[14]]

# # print(res)
# # print(df1.head())

# # df1.append(df1[[columns[5]]].sum().rename('Grandtotal33')).fillna('')

# # '''--->'''
# # df1.loc['GrandTotal'] = df1[[columns[x] for x in range(5,20)]].sum()
# # # df1.loc['GrandTotal55'] = df1.loc['GrandTotal55'].fillna('')

# # # for label, _df in df1.groupby(columns[5],columns[6]):
# # #     print(label)
# # #     print(_df)
# # #     print()

# # writer = pd.ExcelWriter('new_book.xlsx')
# # df1.to_excel(writer, 'new_sheet')
# # writer.save() 