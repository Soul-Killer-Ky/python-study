# -*- coding=utf-8 -*-

import string, random
import redis

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
    code = generate(200)
    r = redis.Redis(host='192.168.199.230', port=6379, db=0, password='123456')
    for i in code:
        r.lpush('code1', i)
