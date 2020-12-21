import xlrd

rb = xlrd.open_workbook(r'C:\Users\elili\Downloads\Ассортимент для системы_от 28.10.20.xlsx')

sh = rb.sheet_by_index(0)

# read header values into the list    
keys = [sh.cell(0, col_index).value for col_index in range(sh.ncols)]

dict_list = []

for row_index in range(1, sh.nrows):
    d = {keys[col_index]: sh.cell(row_index, col_index).value 
         for col_index in range(sh.ncols)}
    dict_list.append(d)

print(dict_list)