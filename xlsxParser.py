# coding=utf-8

import xlrd

# parameters
# *** modify ***
path = 'D:\\codes\\CS4195_Modeling\\'
filename = 'mail.xlsx'

# parse
def parser():
    workbook = xlrd.open_workbook(path+filename)
    sheet = workbook.sheet_by_name('Sheet1')
    num_rows = sheet.nrows
    res = []
    for i in range(1,num_rows):
        res.append(sheet.row_values(i))
    return res