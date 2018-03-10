from collections import OrderedDict
import xlwt, json

with open('./numbers.txt', encoding='UTF-8') as f:
    number_list = json.load(f,object_pairs_hook=OrderedDict)
wb = xlwt.Workbook()
ws = wb.add_sheet('number')
# print(enumerate(number_list))
for row,number_arr in enumerate(number_list):
    # print(enumerate(number_list))
    for col,number in enumerate(number_arr):
        ws.write(row,col,number)
wb.save('./number.xls')