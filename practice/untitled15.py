# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 14:55:48 2022

@author: 15612
"""




import pymysql
import tkinter#图形化的界面的模块
from tkinter.ttk import Treeview
             #消息取拟的模块
from tkinter.messagebox import (showerror, showinfo,askyesno)

def doSql(sql):
    '''用来执行SQL语句'''    
    conn = pymysql.connect(
        #建立通讯
            host = '127.0.0.1',
            user = 'root',#账户
            password = 'Wxy12931293',
            database = 'jw',
            charset = 'utf8'
            ) 
    cur = conn.cursor()#游标
    cur.execute(sql)
    conn.commit()

# 创建tkinter应用程序窗口
root = tkinter.Tk()
# 设置窗口大小和位置
root.geometry('500x600+400+100')
        #   窗口大小    边界
# 不允许改变窗口大小
root.resizable(False, False)
# 设置窗口标题
root.title('通信录管理系统')

# 在窗口上放置标签组件和用于输入姓名的文本框组件
lbtxm = tkinter.Label(root, text='条形码：')
#
lbtxm .place(x=10, y=10, width=47, height=20)
#表示把标签放在到左边10高10
entrytxm  = tkinter.Entry(root)
#建立了文本框
entrytxm .place(x=60, y=10, width=150, height=20)

# 在窗口上放置标签组件和用于选择性别的组合框组件
lbsm = tkinter.Label(root, text='书名：')
lbsm.place(x=220, y=10, width=40, height=20)
# combosm = tkinter.ttk.Combobox(root,
#                                 values=('男', '女'))
# combosm.place(x=270, y=10, width=150, height=20)
entrysm  = tkinter.Entry(root)
entrysm .place(x=270, y=10, width=150, height=20)
# 在窗口上放置标签组件和用于输入年龄的文本框组件
lbflh = tkinter.Label(root, text='分类号：')
lbflh.place(x=10, y=50, width=47, height=20)
entryflh = tkinter.Entry(root)
entryflh.place(x=60, y=50, width=150, height=20)

# 在窗口上放置标签组件和用于输入部门的文本框组件
lbzz = tkinter.Label(root, text='作者：')
lbzz.place(x=220, y=50, width=40, height=20)
entryzz = tkinter.Entry(root)
entryzz.place(x=270, y=50, width=150, height=20)

# 在窗口上放置标签组件和用于输入电话号码的文本框组件
lbcbs= tkinter.Label(root, text='出版社：')
lbcbs.place(x=10, y=90, width=47, height=20)
entrycbs = tkinter.Entry(root)
entrycbs.place(x=60, y=90, width=150, height=20)

# 在窗口上放置标签组件和用于输入QQ号码的文本框组件
lbcbrq = tkinter.Label(root, text='出版日期：')
lbcbrq.place(x=223, y=90, width=58, height=20)
entrycbrq = tkinter.Entry(root)
entrycbrq.place(x=280, y=90, width=140, height=20)
#

lbsj = tkinter.Label(root, text='售价：')
lbsj.place(x=10, y=130, width=40, height=20)
entrysj = tkinter.Entry(root)
entrysj.place(x=60, y=130, width=150, height=20)

lbdclb = tkinter.Label(root, text='包装：')
lbdclb.place(x=220, y=130, width=40, height=20)
entrydclb = tkinter.Entry(root)
entrydclb.place(x=270, y=130, width=150, height=20)


lbzk = tkinter.Label(root, text='租客：')
combozk = tkinter.ttk.Combobox(root,
                                values=('0', '1'))
#有租客为1，无租客为0
lbzk.place(x=10, y=170, width=40, height=20)
entryzk= tkinter.Entry(root)
entryzk.place(x=60, y=170, width=150, height=20)

lbbz = tkinter.Label(root, text='货币：')
lbbz.place(x=220, y=170, width=40, height=20)
entrybz = tkinter.Entry(root)
entrybz.place(x=270, y=170, width=150, height=20)


lbjj = tkinter.Label(root, text='简介')
lbjj.place(x=10, y=210, width=40, height=20)
entryjj = tkinter.Entry(root)
entryjj.place(x=60, y=210, width=150, height=20)



# 在窗口上放置用来显示通信录信息的表格，使用Treeview组件实现
frame = tkinter.Frame(root)
frame.place(x=0, y=280, width=480, height=280)
# 滚动条
scrollBar = tkinter.Scrollbar(frame)
scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
#Treeview组件
treelibrary = Treeview(frame,columns=('c1', 'c2','c3','c4','c5', 'c6','c7','c8','c9','c10','c11'),show="headings",yscrollcommand=scrollBar.set)
treelibrary.column('c1', width=70, anchor='center')
treelibrary.column('c2', width=40, anchor='center')
treelibrary.column('c3', width=40, anchor='center')
treelibrary.column('c4', width=120, anchor='center')
treelibrary.column('c5', width=100, anchor='center')
treelibrary.column('c6', width=90, anchor='center')
treelibrary.column('c5', width=120, anchor='center')
treelibrary.column('c6', width=120, anchor='center')
treelibrary.column('c7', width=120, anchor='center')
treelibrary.column('c8', width=120, anchor='center')
treelibrary.column('c9', width=120, anchor='center')
treelibrary.column('c10', width=120, anchor='center')
treelibrary.column('c11', width=120, anchor='center')








treelibrary.heading('c1', text='条形码')
treelibrary.heading('c2', text='书名')
treelibrary.heading('c3', text='分类号')
treelibrary.heading('c4', text='作者')
treelibrary.heading('c5', text='出版社')
treelibrary.heading('c6', text='出版日期')
treelibrary.heading('c7', text='售价')
treelibrary.heading('c8', text='包装')
treelibrary.heading('c9', text='租客')
treelibrary.heading('c10', text='货币')
treelibrary.heading('c11', text='简介')





treelibrary.pack(side=tkinter.LEFT, fill=tkinter.Y)
#place是精确定位，pack是指定位置
# Treeview组件与垂直滚动条结合
scrollBar.config(command=treelibrary.yview)

# 定义Treeview组件的左键单击事件，并绑定到Treeview组件上
# 单击鼠标左键，设置变量nameToDelete的值，然后可以使用“删除”按钮来删除
nameToDelete = tkinter.StringVar('')
def treeviewClick(event):
    if not treelibrary.selection():
        return
    item = treelibrary.selection()[0]
   
    name = treelibrary.item(item, 'values')[0]
  
    nameToDelete.set(name)
treelibrary.bind('<ButtonRelease-1>', treeviewClick)

def bindData():
    '''把数据库里的通信录记录读取出来，然后在表格中显示'''
    # 删除表格中原来的所有行
    for row in treelibrary.get_children():
        #print(row)
        treelibrary.delete(row)
        
    # 读取数据库中的所有数据
    conn = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            password = '422678116',
            database = 'library',
            charset = 'utf8'
            ) 
    cur = conn.cursor()
    cur.execute('SELECT * FROM library ORDER BY id ASC')
    temp = cur.fetchall()    
    # 把数据插入表格
    for i, item in enumerate(temp):
        treelibrary.insert('', i, values=item[1:])
# 调用函数，把数据库中的记录显示到表格中
bindData()#绑定函数

# 在窗口上放置用于添加通信录的按钮，并设置按钮单击事件函数
def buttonAddClick():
    # 检查姓名
    txm = entrytxm.get().strip()
    #                获取内容

    if not txm:#如果为空
        showerror(title='很抱歉', message='必须输入条形码')
        return
    
    # 姓名不能重复
    conn = pymysql.connect(
           host = '127.0.0.1',
           user = 'root',
           password = 'Wxy12931293',
           database = 'jw',
           charset = 'utf8'
           ) 
    cur = conn.cursor()
    sql = f'SELECT COUNT(id) FROM library WHERE txm="{txm}"'#从后台去查找如果不等于0就说明重复了
    cur.execute(sql)
    c = cur.fetchone()[0]
    if c != 0:
        showerror(title='很抱歉', message='条形码不能重复')
        return
    
    # 获取选择的性别
    # sex = comboSex.get()
    # if sex not in '男女':
    #     showerror(title='很抱歉', message='性别不合法')
    #     return
    
    # 检查年龄
    # age = entryAge.get().strip()
    # if not (age.isdigit() and 1<int(age)<100):
    #     showerror(title='很抱歉',
    #               message='年龄必须为1到100之间的数字')
        # return


    sm = entrysm.get().strip()
    #                获取内容

    if not sm:#如果为空
        showerror(title='很抱歉', message='必须输入书名')
        return

       






    # 检查部门
    flh = entryflh.get().strip()
    if not flh:
        showerror(title='很抱歉', message='必须输入分类号')
        return
    
    # 检查电话号码
    zz = entryzz.get().strip()
    if not zz:
        showerror(title='很抱歉',
                  message='必须输入作者')
        return
    
    # 检查QQ号码.isdigit()
    cbs = entrycbs.get().strip()
    if not cbs.isdigit():
        showerror(title='很抱歉',
                  message='必须输入出版社')
        return
    
    cbrq = entrycbrq.get().strip()
    if not cbrq:
        showerror(title='很抱歉',
                  message='必须输入出版日期')
        return
    
    sj = entrysj.get().strip()
    if not sj.isdigit():
        showerror(title='很抱歉',
                  message='必须输入售价')
        return
    
    dclb = entrydclb.get().strip()
    if not dclb:
        showerror(title='很抱歉',
                  message='必须输入包装方式')
        return
    
    zk = entryzk.get().strip()
    if not zk:
        showerror(title='很抱歉',
                  message='必须输入租客')
        return
    
    bz = entrybz.get().strip()

    
    
    jj = entryjj.get().strip()
    
      
    
    
    
    
    
    
    
    
    # 所有输入都通过检查，插入数据库"{}"
    sql = (f'INSERT INTO library(txm,sm,flh,'+
           f'zz,cbs,cbrq,sj,dclb,zk,bz,jj)'+
           f'VALUES("{txm}","{sm}","{flh}",'+
           f'"{zz}",{cbs}","{cbrq}","{sj}","{dclb}","{zk}","{bz}","{jj}")')
    doSql(sql)
    
    # 添加记录后，更新表格中的数据
    bindData()
buttonAdd = tkinter.Button(root, text='添加',
                           command=buttonAddClick)
buttonAdd.place(x=120, y=250, width=80, height=20)

# 在窗口上放置用于删除通信录的按钮，并设置按钮单击事件函数
def buttonDeleteClick():
    txm = nameToDelete.get()#把姓名给这个变量
    if txm == '':
        showerror(title='很抱歉', message='请选择一条记录')
        return
    
    # 如果已经选择了一条通信录，执行SQL语句将其删除
    sql = f'DELETE FROM library WHERE txm="{txm}"'
    if askyesno('请确认', '确定要删除') == tkinter.YES:
        doSql(sql)
        showinfo('恭喜', '删除成功')    
        # 重新设置变量为空字符串
        nameToDelete.set('')
        # 更新表格中的数据
        bindData()
buttonDelete = tkinter.Button(root, text='删除',
                              command=buttonDeleteClick)
buttonDelete.place(x=240, y=250, width=80, height=20)

# 启动消息主循环，启动应用程序
root.mainloop()
