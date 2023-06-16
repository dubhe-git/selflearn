#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：selflearn 
@IDE     ：PyCharm 
@Author  ：Dubhe
@Date    ：2023/5/15 01:35 
'''

import psycopg2

try:
    conn = psycopg2.connect(
        database="test",
        user="postgres",
        password="422678116",
        host="localhost",
        port="5432"
    )
    print("连接成功")

    # 切换到 test 数据库
    cursor = conn.cursor()
    cursor.execute("SET search_path TO test")

    # 查询 test 数据库中所有表的信息
    cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'test'")
    table_names = cursor.fetchall()
    cursor.execute("SELECT * FROM test.mygame")
    result = cursor.fetchall()
    print(result)
    if len(table_names) > 0:
        print("所有表格名称：")
        for table in table_names:
            print(table[0])
    else:
        print("没有找到表格")

    # 关闭连接
    cursor.close()
    conn.close()
except Exception as e:
    print("连接失败：", e)


