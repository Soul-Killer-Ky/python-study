import sys
import string

path = "filterred_words.txt"

l = list()

with open(path, encoding='UTF-8') as f:
    l = f.read().splitlines()

print(l)

while (True):
    key = input()
    if key == 'close':
        break
    for x in l:
        result = key.replace(x, '*' * len(x))
        key = result
    print(result)

