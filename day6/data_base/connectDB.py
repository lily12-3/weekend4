# coding=utf-8
#首先导入pymql代码库

import pymysql


def connDb():
    conn = pymysql.Connect(host="127.0.0.1", user="root", password="root", database="pirate", port=3306, charset='utf8')
    sql = "select * from hd_user order by id desc"
    curs = conn.cursor()
    curs.execute(sql)
    result = curs.fetchone()

    return result

if __name__ == '__main__':
    print(connDb())