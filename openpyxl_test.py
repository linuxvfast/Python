import openpyxl

# defind sheet title
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.title = 'Spam Bacon Eggs Sheet'
# print(wb.get_sheet_names())


# rename sheet title and save
# wb = openpyxl.open('example.xlsx')
# sheet = wb.active
# sheet.title = 'Spam'
# wb.save('example_copy.xlsx')

# work table create and remove
# wb = openpyxl.Workbook()
# wb.create_sheet()
# print(wb.create_sheet(index=0,title='First Sheet'))
# print(wb.create_sheet(index=2,title='Second Sheet'))
# print(wb.get_sheet_names())
# wb.remove_sheet(wb.get_sheet_by_name('Second Sheet'))
# wb.remove_sheet(wb.get_sheet_by_name('Sheet1'))
# print(wb.get_sheet_names())


# value insert the table
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet['A1']='Hello World'
# print(sheet['A1'].value)
# wb.save('res.xlsx')

# ===================更新Excel数据==============================
'''
# update table
wb = openpyxl.open('produceSales.xlsx')
sheet = wb.active

# update the prices
PRICE_UPDATES = {
    'Garlic': 3.07,
    'Celery': 1.19,
    'Lemon': 1.27
}

# TODO: Loop through the rows and update the prices.
for rowNum in range(2, sheet.max_row + 1):
    produceName = sheet.cell(row=rowNum, column=1).value
    if produceName in PRICE_UPDATES:
        sheet.cell(row=rowNum, column=2).value = PRICE_UPDATES[produceName]
wb.save('updateProduceSales.xlsx')
'''

# ===================设置单元格的字体风格==============================