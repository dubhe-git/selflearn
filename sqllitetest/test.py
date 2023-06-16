#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：selflearn 
@IDE     ：PyCharm 
@Author  ：Dubhe
@Date    ：2023/5/12 22:59 
'''

import sqlite3


def do_sql(sql):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    print(sql)
    cursor.close()
    conn.close()
    print("suuce")


def do_many(sql):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(sql)
    cursor.close()
    conn.close()
    print(result)


def insert_member():
    a = input("please input member_name \n")
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO member(name, status) VALUES ('{}', 0)".format(a))
    conn.commit()

    last_id = cursor.lastrowid  # 获取最后插入的行的 id
    print("last inserted id: ", last_id)

    # 使用 last_id 进行查询操作
    cursor.execute("SELECT * FROM member WHERE id = ?", str(last_id))
    result = cursor.fetchall()
    print(result)

    # print(sql)

    cursor.close()
    conn.close()



def show_member():
    sql = "select * from member;"
    do_many(sql)


while True:
    choice = input("请输入操作指令：1：插入会员数据 2：查询当前所有会员信息 e:退出当前程序\n")
    if choice == "1":
        insert_member()
    elif choice == "2":
        show_member()
    elif choice.lower() == "e":
        print("退出程序")
        exit()
    else:
        print("error")
        continue
