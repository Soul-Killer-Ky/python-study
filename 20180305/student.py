import json, xlwt
from collections import OrderedDict

with open('./student.txt', encoding='UTF-8') as f:
    student_dict = OrderedDict(json.load(f))
    # print(student_dict.items())

wb = xlwt.Workbook()
ws = wb.add_sheet('student')

row = 0
for k,v in student_dict.items():
    ws.write(row, 0, k)
    col = 1
    for item in v:
        ws.write(row, col, item)
        col += 1
    row += 1
wb.save('student.xls')
