# -*- coding=utf-8 -*-

dict1 = {}

with open('./test.txt', 'r') as f:
    while True:
        tmp = f.read(1)
        if not tmp:
            break
    # print(tmp)
        dict1[tmp] = dict1.get(tmp, 0) + 1
    # if dict1[tmp]:
    #     dict1[tmp] += 1
    # else:
    #     dict1[tmp] = 1

print(dict1)
