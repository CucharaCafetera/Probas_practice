import openpyxl as op
wb=op.Workbook()
ws=wb.active
ws.title="Datos"
datos=[["Producto","Cantidad","Precio"],["Manzanas",50,0.5],["Naranjas",30,0.75]]
for x in datos:
    ws.append(x)
wb.save("Ventas.xlsx")