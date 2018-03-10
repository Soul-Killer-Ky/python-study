# -*- coding=utf-8 -*-

import os, string, re

path = "D:\phpStudy\WWW\gaore\op-group.gaore.com"
os.chdir(path)

fh=open('index.php', encoding='UTF-8')
read_fh=fh.readlines()
fh.close()
number_code=0
number_empty=0
number_note=0
pattern='(.*?#|.*?//)' # 正则匹配模式

for x in read_fh:
    # 计算注释数目
    t = '//'
    if '#' in x or t in x:
        tmp1 = re.findall(pattern, x)
        tmp = re.findall(pattern, x)[0][:-1]
        if tmp.isspace() or tmp == '' or tmp == '/':
            number_note += 1
        else:
            number_code += 1

    elif x.isspace():
        number_empty += 1
    else:
        number_code += 1
print('code number is %d'%(number_code+number_empty+number_note))
print('empty number is %d'%number_empty)
print('note number is %d'%number_note)