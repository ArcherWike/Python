from openpyxl import Workbook 
from openpyxl.chart import BarChart, Reference, Series 

wb = Workbook()
ws = wb.active

for i in range(0,30, 2):
    ws.append([i])

values = Reference(ws, min_col=1, min_row=1, max_col=1, max_row=15)
chart = BarChart()
chart.add_data(values)

ws.add_chart(chart, "C5")

wb.save("chart.xlsx")