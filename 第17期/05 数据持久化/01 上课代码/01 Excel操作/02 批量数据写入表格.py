import openpyxl

work = openpyxl.Workbook()
sheet1 = work.active

for i in range(1, 10):

    for j in range(1, i + 1):
        print(f'{j} x {i} = {j * i}', end='\t')
        sheet1.cell(row=i, column=j).value = f'{j} x {i} = {j * i}'
    print()

work.save('实例.xlsx')