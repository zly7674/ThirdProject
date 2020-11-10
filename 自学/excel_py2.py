import openpyxl
book = openpyxl.Workbook()
sh = book.active
sh.title="工资表"
book.save("数据1.xlsx")
sh.cell(1,1,value=1)
book.save("数据1.xlsx")
