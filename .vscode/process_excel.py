from PIL import ImageGrab
import win32com.client as win32
import pandas as pd
import openpyxl

xlApp = win32.gencache.EnsureDispatch('Excel.Application')
xlApp.Visible = True

wb = xlApp.Workbooks.Open(r'C:\Users\elili\Downloads\Ассортимент для системы_от 28.10.20.xlsx', ReadOnly=False)
#df = pd.read_excel(r'C:\Users\elili\Downloads\Ассортимент для системы_от 28.10.20.xlsx')
#print(df.head())

#lastrow = wb.Cells(ws.Rows.Count, 1).End(xlUp).Row + 1
sh = wb.ActiveSheet
print(wb.)
dict = {}
r = 0

for shape in enumerate(sh.Shapes):
    shape.Copy()
    image = ImageGrab.grabclipboard()
    image.save('C:\\Users\\elili\\Downloads\\' + item + '.jpg', 'jpeg')
    r = r + 1


