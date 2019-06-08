import xlrd

wb = xlrd.open_workbook("C:\\Users\\Harish\\Desktop\\book1.xlsx")
ws = wb.sheet_by_name("setup")
# print(ws.cell_value(0, 1))
# print(ws.ncols)
# print(ws.nrows)

col_val = ws.ncols
row_val = ws.nrows


def select_cell_val(input_val):
    for i in range(row_val):
        for j in range(col_val):
            if input_val == ws.cell_value(i, j):
                return ws.cell_value(i + 1, j)
        break


val = select_cell_val("Pwd")
print(val)
