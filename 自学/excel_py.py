import xlrd
book = xlrd.open_workbook("数据.xls")
print(f"表单数量:{book.nsheets}")
print(f"名称分别为:{book.sheet_names()}")
ex1=book.sheet_by_index(0)
ex2=book.sheet_by_name("Sheet1")
print(f"表名:{ex1.name}")
print(f"行数:{ex1.nrows}")
print(f"列数:{ex1.ncols}")
print(f"索引:{ex1.number}")

#某单元格获取
def danrd(x,y):
    print(f"{x,y}的内容为:{ex1.cell_value(rowx=(x-1),colx=(y-1))}")

#某行获取
def rowrd(x):
    print(f"第{x}行:{ex1.row_values(rowx=(x-1),start_colx=1)}")
    infor=ex1.row_values(rowx=(x-1),start_colx=1)
    print(infor[4])

#某列获取
def colrd(y):
    print(f"第{y}列:{ex1.col_values(colx=(y-1),start_rowx=1)}")
#rowrd(67)
def selectinfor():
    for i in range(ex1.nrows):
        infor=ex1.row_values(rowx=(i),start_colx=1)
        #print(infor[5])
        if infor[4]=='未过260':
            print(infor)

selectinfor()


