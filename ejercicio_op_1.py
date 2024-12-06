import openpyxl as op
wb=op.Workbook()
ws=wb.active
ws.title="monki"
wb.save('mi_libro.xlsx')