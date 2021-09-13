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

# def turn_to_cols(x):
#     return columns[x]

# cols = [ x for x in range(0,4)]
# cols_res = map(turn_to_cols, cols)
# print([cols_res])

# print('4'*20)
# df1.loc[:,cols] = df1.loc[:,cols].ffill()
# print(df1.head())
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
# Fill NA with zeros
print(df1.iloc[5,2])
print(df1.head())

df1.replace(np.nan,0)
# for i in range(5, rows):
#     for j in range(2,columns):
#         if df1.iloc[i,j] == NaN:
#             df1[i,j].fillna(0, inplace = True)

print(df1.head())

def assign_quarterly_sum(array_name, quarter_name, row_number, column_number, sheet):
    '''recalculate total by columns'''
    array_name[quarter_name] = 0
    if 'Total' in str(df1.iloc[row,0]) or 'Total' in str(df1.iloc[row,1]) or 'Total' in str(df1.iloc[row,2]):
        pass
    array_name[quarter_name] += df1.iloc[row, column_number]

budget = {}
reforecast = {}
actual = {}

for row in range(1, rows):

    budget_map = {
                'Q1': 5,
                'Q2': 6,
                'Q3': 7,
                'Q4': 8,
                'FY': 9
                }

    reforecast_map = {
                'Q1': 10,
                'Q2': 11,
                'Q3': 12,
                'Q4': 13,
                'FY': 14
                }

    actual_map = {
                'Q1': 15,
                'Q2': 16,
                'Q3': 17,
                'Q4': 18,
                'FY': 19
                }

    assign_quarterly_sum( budget, 'Q1', row, budget_map['Q1'], df1)
    assign_quarterly_sum( budget, 'Q2', row, budget_map['Q2'], df1)
    assign_quarterly_sum( budget, 'Q3', row, budget_map['Q3'], df1)
    assign_quarterly_sum( budget, 'Q4', row, budget_map['Q4'], df1)
    assign_quarterly_sum( budget, 'FY', row, budget_map['FY'], df1)

    assign_quarterly_sum( reforecast, 'Q1', row, reforecast_map['Q1'], df1)
    assign_quarterly_sum( reforecast, 'Q2', row, reforecast_map['Q2'], df1)
    assign_quarterly_sum( reforecast, 'Q3', row, reforecast_map['Q3'], df1)
    assign_quarterly_sum( reforecast, 'Q4', row, reforecast_map['Q4'], df1)
    assign_quarterly_sum( reforecast, 'FY', row, reforecast_map['FY'], df1)
    
    assign_quarterly_sum( actual, 'Q1', row, actual_map['Q1'], df1)
    assign_quarterly_sum( actual, 'Q2', row, actual_map['Q2'], df1)
    assign_quarterly_sum( actual, 'Q3', row, actual_map['Q3'], df1)
    assign_quarterly_sum( actual, 'Q4', row, actual_map['Q4'], df1)
    assign_quarterly_sum( actual, 'FY', row, actual_map['FY'], df1)

print(f'budget: {budget}')
print(f'reforecast: {reforecast}')
print(f'actual: {actual}')







def assign_fy_by_row(array_name, row_number, column_number, sheet):
    '''recalculate total by rows'''
    array_name[row] = 0
    if type(df1.iloc[row,column_number]) == float or type(df1.iloc[row,column_number]) == int:
        array_name[row] += df1.iloc[row,column_number]

budget_recal= {}
april_reforecast_recal= {}
actuals_recal = {}
for row in range(1,rows):
    for column in range(6, 9):
        assign_fy_by_row(budget_recal, row, column, df1)

    for column in range(10, 15):
        assign_fy_by_row(april_reforecast_recal, row, column, df1)

    for column in range(16,20):
        assign_fy_by_row(actuals_recal, row, column, df1)

print(f'budget_recal: {budget_recal}')
print(f'april_reforecast_recal: {april_reforecast_recal}')
print(f'actuals_recal: {actuals_recal}')




# def assign_quarterly_sum_by_clinical_number(array_name, quarter_name, row_number, column_number, sheet):
#     '''recalculate total by clinical study number'''
#     array_name[quarter_name] = 0
#     if 'Total' in str(df1.iloc[row,0]) or 'Total' in str(df1.iloc[row,1]) or 'Total' in str(df1.iloc[row,2]):
#         pass
#     array_name[quarter_name] += df1.iloc[row, column_number]

# header = True
# for row in range(rows):
#     if header:
#         if df1.iloc[row,0] =='Budget Type': 
#             header = False
#             # print(row, 'label row- skip')
#     else:
#         budget = {}
#         reforecast = {}
#         actual = {}

#         assign_quarterly_sum( budget, 'Q1', row, 5, df1)
#         assign_quarterly_sum( budget, 'Q2', row, 6, df1)
#         assign_quarterly_sum( budget, 'Q3', row, 7, df1)
#         assign_quarterly_sum( budget, 'Q4', row, 8, df1)
#         assign_quarterly_sum( budget, 'FY', row, 9, df1)

#         assign_quarterly_sum( reforecast, 'Q1', row, 10, df1)
#         assign_quarterly_sum( reforecast, 'Q2', row, 11, df1)
#         assign_quarterly_sum( reforecast, 'Q3', row, 12, df1)
#         assign_quarterly_sum( reforecast, 'Q4', row, 13, df1)
#         assign_quarterly_sum( reforecast, 'FY', row, 14, df1)
        
#         assign_quarterly_sum( actual, 'Q1', row, 15, df1)
#         assign_quarterly_sum( actual, 'Q2', row, 16, df1)
#         assign_quarterly_sum( actual, 'Q3', row, 17, df1)
#         assign_quarterly_sum( actual, 'Q4', row, 18, df1)
#         assign_quarterly_sum( actual, 'FY', row, 19, df1)

# print(f'budget: {budget}')
# print(f'reforecast: {reforecast}')
# print(f'actual: {actual}')





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