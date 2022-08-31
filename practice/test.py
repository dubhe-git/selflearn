# record = input('请输入 dzzh,xm, xb, sf,dhhm(输入Q/q可以返回菜单，其中逗号应为英文逗号):\n')
#         #输入q或Q表示退出，结束插入记录的过程，返回主菜单
# if record in ('q', 'Q'):
#     print('\t您已经退出了添加读者信息板块')           
       
#         #正确的格式应该恰好包含4个英文逗号
# if record.count(',') != 4:
#     print('\tformat or data error.')
# else:
#     dzzh,xm, xb, sf,dhhm = record.split(',')
#             #性别必须是F或M
#     print(dzzh)
#     print(xm)
#     print(xb)
#     print(sf)
#     print(dhhm)
#     if xb not in ('男', '女'):
#         print('\t性别必须是 男 or 女.')
#             #读者证号和电话号码必须是数字字符串
#     if (not dhhm.isdigit()) or (not dzzh.isdigit()):
#         print('\tdzzh and dhhm must be integers.')


record = "0001,Mary,male,student,1331"
dzzh,xm, xb, sf,dhhm = record.split(',')
print(dzzh)
print(xm)
print(xb)
print(sf)
print(dhhm)

# sql = 'INSERT INTO reader VALUES('+record+')'
# print(sql)

data = dzzh,xm,xb,sf,dhhm
sql = 'INSERT INTO reader VALUES{}'.format(data)

sql1 = 'INSERT INTO reader VALUES('+record+")"
print(sql1)
print(sql)