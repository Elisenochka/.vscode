import xlrd
import pandas as pd
import requests

rb = xlrd.open_workbook(r"C:\Users\elili\Downloads\Ejecuciones 26.10.2020.xls")
sh = rb.sheet_by_name("Datos")
num_rows = sh.nrows - 1
num_cells = sh.ncols - 1

filePath = r"C:\Users\elili\Documents\IntelligenceRetail\Nestle\foto_lot_2"

curr_row = 1

while curr_row < num_rows:
    image_url = sh.cell_value(curr_row, num_cells)
    sku = sh.cell_value(curr_row, num_cells - 1)
    img_data = requests.get(image_url).content
    with open(filePath +  "\\" + sku + str(curr_row) + ".jpg", 'wb') as handler:
        handler.write(img_data)
    curr_row += 1

df = pd.read_excel(r"C:\Users\elili\Downloads\Ejecuciones 26.10.2020.xls", sheet_name="Datos")
print(df)


img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)