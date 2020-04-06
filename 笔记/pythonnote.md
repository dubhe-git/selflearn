# CSV模块
> `官方文档地址` 
> https://yiyibooks.cn/xx/python_352/library/csv.html#module-csv


## 为什么使用CSV模块
你是不是会困惑，明明前面csv写入我们可以直接用open函数来写，为什么现在还要先引用csv模块？答案：直接运用别人写好的模块，比我们使用open()函数来读写，语法更简洁，功能更强大，待会你就能感受到。那么，何乐而不为？

## CSV模块的引用

```python
import csv
#引用csv模块。
csv_file = open('demo.csv','w',newline='',encoding='utf-8')
#创建csv文件，我们要先调用open()函数，传入参数：文件名“demo.csv”、写入模式“w”、newline=''、encoding='utf-8'。
```

# Excel 相关模块
> `官方文档地址` 
> https://openpyxl.readthedocs.io/en/stable/
## openpyxl 模块
### 安装方法
window电脑：在终端输入命令：
```
pip install openpyxl
```
mac电脑：在终端输入命令：
```
pip3 install openpyxl
```

###使用方法

#### 写入
```python
import openpyxl 
wb=openpyxl.Workbook() 
sheet=wb.active
sheet.title='new title'
sheet['A1'] = '漫威宇宙'
rows= [['美国队长','钢铁侠','蜘蛛侠'],['是','漫威','宇宙', '经典','人物']]
for i in rows:
    sheet.append(i)
print(rows)
wb.save('Marvel.xlsx')
```

#### 读取
```python
import openpyxl 
#写入的代码：
wb = openpyxl.Workbook() 
sheet = wb.active
sheet.title = 'new title'
sheet['A1'] = '漫威宇宙'
rows = [['美国队长','钢铁侠','蜘蛛侠','雷神'],['是','漫威','宇宙', '经典','人物']]
for i in rows:
    sheet.append(i)
print(rows)
wb.save('Marvel.xlsx')

#读取的代码：
wb = openpyxl.load_workbook('Marvel.xlsx')
sheet = wb['new title']
sheetname = wb.sheetnames
print(sheetname)
A1_cell = sheet['A1']
A1_value = A1_cell.value
print(A1_value)
```