import openpyxl
path = "excel.xlsx"
workbook = openpyxl.load_workbook(path)

sheet = workbook.active

cell_1 = sheet["A1:B2"]

for i in cell_1:
    for j in i:
        print("{:<30}".format(j.value) + "{:>30}".format("进步"))