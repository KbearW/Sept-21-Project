import pandas as pd
import numpy as np

xls = pd.ExcelFile('Testing file 9.7.xlsx')
df1 = pd.read_excel(xls, 'REGN Pral Clinical Studies')

rows, columns = df1.shape 

col_list = df1.columns.tolist()

label_cols = col_list[0:5]
data_cols = col_list[5:]

# print(col_list)
# print(data_cols)
# print(label_cols)

def ffill_blanks(cols):
    '''forward fill blanks'''
    for col in cols:
        df1[col].ffill(inplace = True)

def fill_na(cols):
    '''fill Nan with zeroes'''
    for col in cols:
        df1[col].fillna(0,inplace= True)
        

ffill_blanks(label_cols)
fill_na(data_cols)

###############################################################################
def assign_quarterly_sum(array_name, quarter_name, row_number, column_number, sheet):
    '''recalculate total by columns'''
    array_name[quarter_name] = 0
    if 'Total' in str(df1.iloc[row,0]) or 'Total' in str(df1.iloc[row,1]) or 'Total' in str(df1.iloc[row,2]):
        pass
    array_name[quarter_name] += df1.iloc[row, column_number]

budget = {}
reforecast = {}
actual = {}
actuals_vs_budget = {}
actuals_vs_april = {}

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
    
    var_actuals_vs_budget_map = {
                'Q1': 20,
                'Q2': 21,
                'Q3': 22,
                'Q4': 23,
                'FY': 24
                }

    var_actuals_vs_april_map = {
                'Q1': 25,
                'Q2': 26,
                'Q3': 27,
                'Q4': 28,
                'FY': 29
                }

    assign_quarterly_sum( budget, data_cols[0], row, budget_map['Q1'], df1)
    assign_quarterly_sum( budget, data_cols[1], row, budget_map['Q2'], df1)
    assign_quarterly_sum( budget, data_cols[2], row, budget_map['Q3'], df1)
    assign_quarterly_sum( budget, data_cols[3], row, budget_map['Q4'], df1)
    assign_quarterly_sum( budget, data_cols[4], row, budget_map['FY'], df1)

    assign_quarterly_sum( reforecast, data_cols[5], row, reforecast_map['Q1'], df1)
    assign_quarterly_sum( reforecast, data_cols[6], row, reforecast_map['Q2'], df1)
    assign_quarterly_sum( reforecast, data_cols[7], row, reforecast_map['Q3'], df1)
    assign_quarterly_sum( reforecast, data_cols[8], row, reforecast_map['Q4'], df1)
    assign_quarterly_sum( reforecast, data_cols[9], row, reforecast_map['FY'], df1)
    
    assign_quarterly_sum( actual, data_cols[10], row, actual_map['Q1'], df1)
    assign_quarterly_sum( actual, data_cols[11], row, actual_map['Q2'], df1)
    assign_quarterly_sum( actual, data_cols[12], row, actual_map['Q3'], df1)
    assign_quarterly_sum( actual, data_cols[13], row, actual_map['Q4'], df1)
    assign_quarterly_sum( actual, data_cols[14], row, actual_map['FY'], df1)

    assign_quarterly_sum( actuals_vs_budget, data_cols[15], row, var_actuals_vs_budget_map['Q1'], df1)
    assign_quarterly_sum( actuals_vs_budget, data_cols[16], row, var_actuals_vs_budget_map['Q2'], df1)
    assign_quarterly_sum( actuals_vs_budget, data_cols[17], row, var_actuals_vs_budget_map['Q3'], df1)
    assign_quarterly_sum( actuals_vs_budget, data_cols[18], row, var_actuals_vs_budget_map['Q4'], df1)
    assign_quarterly_sum( actuals_vs_budget, data_cols[19], row, var_actuals_vs_budget_map['FY'], df1)
    
    assign_quarterly_sum( actuals_vs_april, data_cols[20], row, var_actuals_vs_april_map['Q1'], df1)
    assign_quarterly_sum( actuals_vs_april, data_cols[21], row, var_actuals_vs_april_map['Q2'], df1)
    assign_quarterly_sum( actuals_vs_april, data_cols[22], row, var_actuals_vs_april_map['Q3'], df1)
    assign_quarterly_sum( actuals_vs_april, data_cols[23], row, var_actuals_vs_april_map['Q4'], df1)
    assign_quarterly_sum( actuals_vs_april, data_cols[24], row, var_actuals_vs_april_map['FY'], df1)
# print(f'budget: {budget}')
# print(f'reforecast: {reforecast}')
# print(f'actual: {actual}')
# print(f'actuals_vs_budget: {actuals_vs_budget}')

res = {**budget, **reforecast, **actual, **actuals_vs_budget, **actuals_vs_april}
df1.loc['recal'] = res
df1.loc['variance'] = df1.loc[11]-df1.loc['recal']

# print(res)


#######################################################################################



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
        budget_recal[0] = 'budget_recal'

    for column in range(10, 15):
        assign_fy_by_row(april_reforecast_recal, row, column, df1)
        april_reforecast_recal[0] = 'april_reforecast_recal'

    for column in range(16,20):
        assign_fy_by_row(actuals_recal, row, column, df1)
        actuals_recal[0] = 'actuals_recal'

# print(f'budget_recal: {budget_recal}')
# print(f'april_reforecast_recal: {april_reforecast_recal}')
# print(f'actuals_recal: {actuals_recal}')

df1[''] = ''
df1['budget_recal'] = pd.DataFrame.from_dict(budget_recal, orient = 'index')
df1['april_reforecast_recal'] = pd.DataFrame.from_dict(april_reforecast_recal, orient = 'index')
df1['actuals_recal'] = pd.DataFrame.from_dict(actuals_recal, orient = 'index')
df1[''] = ''

# variance_act_act = df1['actuals_recal'] - df1['april_reforecast_recal'] 
# print(variance_act_act)

actuals_recal = pd.DataFrame(df1, columns = ['actuals_recal'])
april_reforecast_recal = pd.DataFrame(df1, columns = ['april_reforecast_recal'])
apr_act_var_imported = pd.DataFrame(df1, columns = ['Unnamed: 29'])

print(actuals_recal)
print(april_reforecast_recal)
print(apr_act_var_imported)


# this doesn't work..
print((actuals_recal-april_reforecast_recal))

# df1['(act - april) - variance'] = actuals_recal - april_reforecast_recal - apr_act_var_imported

#######################################################################################

writer = pd.ExcelWriter('new_book.xlsx')
df1.to_excel(writer, 'new_sheet')
writer.save() 