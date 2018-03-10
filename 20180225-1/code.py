# -*- coding=utf-8 -*-

import string, random

field = string.ascii_letters + string.digits

def getRandom(n):
    return "".join(random.sample(field, n))

def cancatenate(g):
    return "-".join([getRandom(4)
                     for i in range(g)])

def generate(n):
    return [cancatenate(4)
            for i in range(n)]

if __name__ == "__main__":
    print(generate(200))