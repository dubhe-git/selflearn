
from enum import auto
from pickle import TRUE
from re import T
import pymysql
import tkinter
from tkinter.ttk import Treeview
from tkinter.messagebox import showerror, showinfo,askyesno

def doSql(sql):
    '''用来执行SQL语句'''    
    conn = pymysql.connect(
        #建立通讯
            host = '127.0.0.1',
            user = 'root',
            password = '422678116',
            database = 'library',
            charset = 'utf8'
            ) 
    cur = conn.cursor()#游标
    cur.execute(sql)
    conn.commit()


# 创建tkinter应用程序窗口
root = tkinter.Tk()
# 设置窗口大小和位置
root.geometry('1280x800+400+100')
        #   窗口大小    边界
# 不允许改变窗口大小
root.resizable(True,True)
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
frame.place(x=0, y=280, width=1080, height=600)
# 滚动条
scrollBar = tkinter.Scrollbar(frame)
scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
#Treeview组件
treebook = Treeview(frame,columns=('c1', 'c2','c3','c4','c5', 'c6','c7','c8','c9','c10','c11'),show="headings",yscrollcommand=scrollBar.set)
treebook.column('c1', width=100, anchor='center')
treebook.column('c2', width=100, anchor='center')
treebook.column('c3', width=40, anchor='center')
treebook.column('c4', width=120, anchor='center')
treebook.column('c5', width=100, anchor='center')
treebook.column('c6', width=90, anchor='center')
treebook.column('c5', width=120, anchor='center')
treebook.column('c6', width=120, anchor='center')
treebook.column('c7', width=120, anchor='center')
treebook.column('c8', width=120, anchor='center')
treebook.column('c9', width=120, anchor='center')
treebook.column('c10', width=120, anchor='center')
treebook.column('c11', width=120, anchor='center')


treebook.heading('c1', text='条形码')
treebook.heading('c2', text='书名')
treebook.heading('c3', text='分类号')
treebook.heading('c4', text='作者')
treebook.heading('c5', text='出版社')
treebook.heading('c6', text='出版日期')
treebook.heading('c7', text='售价')
treebook.heading('c8', text='包装')
treebook.heading('c9', text='租客')
treebook.heading('c10', text='货币')
treebook.heading('c11', text='简介')


treebook.pack(side=tkinter.LEFT, fill=tkinter.Y)
#place是精确定位，pack是指定位置
# Treeview组件与垂直滚动条结合
scrollBar.config(command=treebook.yview)

# 定义Treeview组件的左键单击事件，并绑定到Treeview组件上
# 单击鼠标左键，设置变量nameToDelete的值，然后可以使用“删除”按钮来删除
nameToDelete = tkinter.StringVar()
def treeviewClick(event):
    if not treebook.selection():
        return
    item = treebook.selection()[0]
   
    name = treebook.item(item, 'values')[0]
  
    nameToDelete.set(name)
treebook.bind('<ButtonRelease-1>', treeviewClick)

def bindData():
    '''把数据库里的通信录记录读取出来，然后在表格中显示'''
    # 删除表格中原来的所有行
    # for row in treebook.get_children():
    #     #print(row)
    #     treebook.delete(row)
        
    # 读取数据库中的所有数据
    conn = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            password = '422678116',
            database = 'library',
            charset = 'utf8'
            ) 
    cur = conn.cursor()
    cur.execute('SELECT * FROM book ORDER BY txm ASC')
    temp = cur.fetchall()    
    # 把数据插入表格
    for i, item in enumerate(temp):
        treebook.insert('', i, values=item[:])
# 调用函数，把数据库中的记录显示到表格中
bindData()#绑定函数

# 在窗口上放置用于添加通信录的按钮，并设置按钮单击事件函数
def buttonAddClick():
    # 检查姓名
    
    #                获取内容

    # if not txm:#如果为空
    #     showerror(title='很抱歉', message='必须输入条形码')
    #     return
    
    # 姓名不能重复
    # conn = pymysql.connect(
    #        host = '127.0.0.1',
    #        user = 'root',
    #        password = '422678116',
    #        database = 'library',
    #        charset = 'utf8'
    #        ) 
    # cur = conn.cursor()
    # sql = 'SELECT COUNT(id) FROM book WHERE txm="{}"'.format(txm)#从后台去查找如果不等于0就说明重复了
    # cur.execute(sql)
    # c = cur.fetchone()[0]
    # if c != 0:
    #     showerror(title='很抱歉', message='条形码不能重复')
    #     return

    
    #                获取内容

    # if not sm:
    #     showerror(title='很抱歉', message='必须输入书名')
    #     return

       
    
    # if not flh:
    #     showerror(title='很抱歉', message='必须输入分类号')
    #     return

    
    # if not zz:
    #     showerror(title='很抱歉',message='必须输入作者')
    #     return
    
    # if not cbs.isdigit():
    #     showerror(title='很抱歉',message='必须输入出版社')
    #     return
    
    
    # if not cbrq:
    #     showerror(title='很抱歉',message='必须输入出版日期')
    #     return
    
    
    # if not sj.isdigit():
    #     showerror(title='很抱歉',message='必须输入售价')
    #     return
    
    
    # if not dclb:
    #     showerror(title='很抱歉',message='必须输入包装方式')
    #     return
    
    # if not zk:
    #     showerror(title='很抱歉',message='必须输入租客')
    #     return
    
    txm = entrytxm.get().strip()
    sm = entrysm.get().strip()
    flh = entryflh.get().strip()
    zz = entryzz.get().strip()
    cbs = entrycbs.get().strip()
    sj = entrysj.get().strip()
    cbrq = entrycbrq.get().strip()
    dclb = entrydclb.get().strip()
    zk = entryzk.get().strip()
    bz = entrybz.get().strip()
    jj = entryjj.get().strip()

    
    

    data = txm,sm,flh,zz,cbs,cbrq,sj,dclb,zk,bz,jj
    
    # 所有输入都通过检查，插入数据库"{}"
    sql = 'INSERT INTO book VALUES{}'.format(data)
    doSql(sql)
    
    # 添加记录后，更新表格中的数据
    bindData()
buttonAdd = tkinter.Button(root, text='添加',command=buttonAddClick)
buttonAdd.place(x=120, y=250, width=80, height=20)

# 在窗口上放置用于删除通信录的按钮，并设置按钮单击事件函数
def buttonDeleteClick():
    txm = nameToDelete.get()#把姓名给这个变量
    if txm == '':
        showerror(title='很抱歉', message='请选择一条记录')
        return
    
    # 如果已经选择了一条通信录，执行SQL语句将其删除
    sql = f'DELETE FROM book WHERE txm="{txm}"'
    if askyesno('请确认', '确定要删除') == tkinter.YES:
        doSql(sql)
        showinfo('恭喜', '删除成功')    
        # 重新设置变量为空字符串
        nameToDelete.set('')
        # 更新表格中的数据
        bindData()
buttonDelete = tkinter.Button(root, text='删除',command=buttonDeleteClick)
buttonDelete.place(x=240, y=250, width=80, height=20)

# 启动消息主循环，启动应用程序
root.mainloop()
