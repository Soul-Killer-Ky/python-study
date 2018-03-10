import json, xlwt
from collections import OrderedDict

with open('./city.txt', encoding='UTF-8') as f:
    city_dict = OrderedDict(json.load(f))

row = 0
wb = xlwt.Workbook()
ws = wb.add_sheet('city')

for k,v in city_dict.items():
    print(k, v)
    ws.write(row, 0, k)
    col = 1
    ws.write(row, col, v)
    row += 1
wb.save('./city.xls')