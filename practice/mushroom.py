# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:34:15 2022

@author: 35731
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:37:44 2022

@author: ASUS
"""
import sqlite3


def menu():
    '''本函数用来显示主菜单'''

    usage = ('\tL/l: 显示',
             '\tD/d: 删除',
             '\tA/a: 添加',
             '\tQ/q: 退出',
             '\tH/h: 帮助')
    print('菜单'.center(70, '*'))
    for u in usage:
        print(u)


def doSql(sql):
    '''用来执行SQL语句，尤其是INSERT和DELETE语句'''

    conn = sqlite3.connect("test.db"
                           # host='127.0.0.1',
                           # user='root',
                           # password='422678116',
                           # database='library',
                           # charset='utf8'
                           )
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()


def add():
    """本函数用来接收输入，检查格式，然后插入数据库"""

    print('添加读者信息'.center(70, '*'))
    '''
    while True:
        
        dzzh=input('dzzh:')
        xm=input('xm:')
        xb=input('xb:')
        sf=input('sf:')
        dhhm=input('dhhm:')
        sql='INSERT INTO reader VALUES('dzzh','xm','xb','sf','dhhm')'
        doSql(sql)
        print('\t添加成功')
        continue
    
    '''

    # 获取输入，只接受正确格式的数据
    while True:
        record = input('请输入 dzzh,xm, xb, sf,dhhm(输入Q/q可以返回菜单，其中逗号应为英文逗号):\n')
        # 输入q或Q表示退出，结束插入记录的过程，返回主菜单
        if record in ('q', 'Q'):
            print('\t您已经退出了添加读者信息板块')
            return

        # 正确的格式应该恰好包含4个英文逗号
        # if record.count(',') != 4:
        #     print('\tformat or data error.')
        #     continue
        else:
            dzzh, xm, xb, sf, dhhm = record.split(',')
            value01 = [dzzh, xm, xb, sf, dhhm]
            # 性别必须是F或M
            # if xb not in ('男', '女'):
            #     print('\t性别必须是 男 or 女.')
            #     continue
            # #读者证号和电话号码必须是数字字符串
            # if (not dhhm.isdigit()) or (not dzzh.isdigit()):
            #     print('\tdzzh and dhhm must be integers.')
            #     continue
            # dzzh和dhhm的数据类型不太清楚
            # 为什么在添加模块，添加不了信息
            # dzzh的格式应该怎样调整，我预想的是字符串，（这个是依据老师的代码改的，里面的dzzh之前的格式好像是数字，最后显现出来的不是001的样子）

            # else:

            # continue

        # sql = 'INSERT INTO reader VALUES()'

        # sql = 'INSERT INTO reader(dzzh,xm, xb, sf,dhhm)  VALUES("'
        # sql = sql + dzzh + '","' + xm + '","' + xb + '","'
        # sql = sql  + dhhm + '")'

        # 插入不成功，有问题
        # '''
        # sql = 'INSERT INTO reader(dzzh,xm, xb, sf,dhhm) VALUES("'
        # sql = sql + dzzh + '","' + xm + '",' + xb + '","'
        # sql = sql + sf + '","' + dhhm + '")'
        # '''

        # sql='INSERT INTO reader VALUES('dzzh','xm','xb','sf','dhhm')'
        sql = 'INSERT INTO reader VALUES(s%)', value01
        print(sql)
        doSql(sql)
    print('\t添加成功')


def exist(recordId):
    '''本函数用来测试数据表中是否存在recordId的dzzh'''
    # 与后端进行连接
    conn = sqlite3.connect("test.db"
                           # host='127.0.0.1',
                           # user='root',
                           # password='422678116',
                           # database='library',
                           # charset='utf8'
                           )
    cur = conn.cursor()  # 游标，提取信息
    cur.execute('SELECT COUNT(dzzh) from reader where dzzh=' + str(recordId))
    c = cur.fetchone()[0]
    conn.close()
    return c != 0


def remove():
    '''本函数用来接收用户输入的dzzh，并删除数据库中该dzzh对应的记录'''

    print('Delete records'.center(70, '*'))

    while True:
        # 输入q或Q，返回上一级目录
        x = input('Please input the dzzh to delete(Q/q to return):\n')
        if x in ('q', 'Q'):
            print('\tYou have stopped removing record.')
            return

        # 要删除的dzzh必须是字符串，并且已存在于数据库中
        try:
            recordId = str(x)
            if not exist(recordId):
                print('\tThis dzzh does not exists.')
            else:
                sql = 'DELETE FROM reader where dzzh=' + str(x)
                doSql(sql)
                print('\tYou have deleted a record.')
        except:
            print('\tid must be an integer')


def listInformation():
    '''本函数用来查看所有记录'''

    sql = 'SELECT * FROM reader ORDER BY dzzh ASC'
    conn = sqlite3.connect("test.db"
                           # host='127.0.0.1',
                           # user='root',
                           # password='422678116',
                           # database='library',
                           # charset='utf8'
                           )
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    if not result:
        print('\tDatabase has no record at this time.')
    else:
        # 格式化输出所有记录
        print('All records'.center(70, '='))
        print('dzzh    xm     xb    sf     dhhm')
        for record in result:
            print(str(record[0]).ljust(8), end='')
            print(record[1].ljust(7), end='')
            print(record[2].ljust(6), end='')
            print(record[3].ljust(7), end='')
            print(record[4])

        print('=' * 70)
    conn.close()


def main():
    '''系统主函数'''

    print('欢迎来到读者管理系统')
    menu()
    while True:
        command = input('请输入一个指令:')
        if command in ('L', 'l'):
            listInformation()
        elif command in ('D', 'd'):
            remove()
            menu()
        elif command in ('A', 'a'):
            add()
            menu()
        elif command in ('Q', 'q'):
            break
        elif command in ('H', 'h'):
            menu()
        else:
            print('\t不存在该指令')


# 调用主函数，启动系统
main()
