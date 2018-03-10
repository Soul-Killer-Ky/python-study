# -*- coding=utf-8 -*-

import string, random
import pymysql.cursors

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
    connect = pymysql.connect(
        host="192.168.199.230",
        port=3306,
        user="origin",
        passwd="123456",
        db="test",
        charset="utf8"
    )
    cursor = connect.cursor()
    sql = "insert into test(code) values(%s)"
    cursor.executemany(sql, code)
    connect.commit()
    print('成功插入', cursor.rowcount, '条数据')
